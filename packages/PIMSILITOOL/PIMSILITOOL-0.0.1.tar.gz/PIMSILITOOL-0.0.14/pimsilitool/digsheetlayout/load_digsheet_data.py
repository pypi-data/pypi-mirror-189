from logging import exception
import arcpy
import pimsilitool
import os
import datetime as dt
import math
from pimsilitool import config
import traceback
import sys
from arcpy import env
import numpy
import uuid

class load_digsheet_data():
    def __init__(self):
        self.in_anomaly_features = None
        self.in_anomaly_routeid_fld = None
        self.in_anomaly_id_fld = None
        self.in_anomaly_measure_fld = None
        self.in_anomaly_digid_fld = None
        self.in_anomaly_dig_target_fld = None
        self.in_anomaly_priority_fld = None
        self.in_anomaly_priority_values = None

        # Weld parameters
        self.in_weld_features = None
        self.in_weldid_fld = None
        self.in_weld_routeid_fld = None
        self.in_weld_measure_fld = None

        # Right of way parameters
        self.in_row_features = None
        self.in_row_begin_routeid_fld = None
        self.in_row_begin_measure_fld = None
        self.in_row_end_routeid_fld = None
        self.in_row_end_measure_fld = None
        self.in_row_owner_fld = None

        # Dig sheet parameters
        self.in_dig_features = None
        self.in_digsheet_begin_routeid_field = None
        self.in_digsheet_begin_measure_field = None
        self.in_digsheet_end_routeid_field = None
        self.in_digsheet_end_measure_field = None
        self.in_dig_id_fld = None
        self.in_dig_begin_weldid_fld = None
        self.in_dig_begin_weld_measure_fld = None
        self.in_dig_end_weldid_fld = None
        self.in_dig_end_weld_measure_fld = None
        self.in_dig_row_owner_fld = None
        self.in_dig_reason_fld = None
        self.in_dig_reason_value = None
        self.in_dig_status_fld = None
        self.in_dig_status_value = None
        self.in_dig_priority_fld = None
        self.in_dig_priority_value = None
        self.in_dig_project_fld = None
        self.in_dig_project_value = None
        # self.in_dig_revision_fld = None
        # self.in_dig_revision_value = None
        # ds.in_dig_revision_value = parameters[36].valueAsText
        self.in_digsheet_begin_exc_lat_field = None
        self.in_digsheet_begin_exc_long_field = None
        self.in_digsheet_end_exc_lat_field = None
        self.in_digsheet_end_exc_long_field = None

        # engineering station network
        self.in_eng_sta_network_features = None
        self.in_eng_sta_network_unique_id = None
        self.in_eng_sta_network_from_measure = None
        self.in_eng_sta_network_to_measure = None

        # Dig sheet interruption parameters
        self.in_interrupt_features = None
        self.in_interrupt_routeid_fld = None
        self.in_interrupt_id_fld = None
        self.in_interrupt_measure_fld = None
        self.in_interrupt_crossing_width_source = None
        self.in_interrupt_crossing_width_field = None
        self.in_interrupt_crossing_width_value = None

        # default values
        self.in_min_dig_length = None

        # Target anomaly parameters
        self.in_target_anomaly_features = None
        self.in_target_anomaly_routeid_fld = None
        self.in_target_anomalyid_fld = None
        self.in_target_anomaly_digid_fld = None


    def run(self):

        try:
            # get minimum dig length
            if self.in_min_dig_length:
                self.in_min_dig_length = float(self.in_min_dig_length.split(" ")[0])
            else:
                self.in_min_dig_length = 60

            pimsilitool.AddMessage("Anomaly Priority Values: {}".format(self.in_anomaly_priority_values))

            self.create_dig_sheet_events_table()

            self.update_anomaly_target_field()

            ili_fields = [self.in_anomaly_routeid_fld, self.in_anomaly_id_fld, self.in_anomaly_measure_fld,
                          self.in_anomaly_digid_fld,
                          self.in_anomaly_dig_target_fld, self.in_anomaly_priority_fld]

            pimsilitool.AddMessage("Creating Feature Class To NumPy Array...")
            # get anomaly numpy array
            self.in_ili_anomaly_nparr = arcpy.da.FeatureClassToNumPyArray(self.in_anomaly_features, ili_fields, null_value=-9999)

            if len(self.in_ili_anomaly_nparr) < 1:
                pimsilitool.AddWarning("No Anomaly features found!")
                return
            else:
                self.in_ili_anomaly_nparr = numpy.sort(self.in_ili_anomaly_nparr, order=[self.in_anomaly_measure_fld])

            # get girth weld numpy array
            weld_fields = [self.in_weld_routeid_fld, self.in_weldid_fld, self.in_weld_measure_fld, "SHAPE@X", "SHAPE@Y"]
            where_clause = "1 = 1"

            in_weld_nparr = self.convert_fc2np(self.in_weld_features, weld_fields, where_clause)
            if len(in_weld_nparr) < 1:
                pimsilitool.AddWarning("No Girth Weld features found!")
                return

            # get right of way numpy array
            row_fields = [self.in_row_begin_routeid_fld, self.in_row_begin_measure_fld,
                          self.in_row_end_routeid_fld, self.in_row_end_measure_fld, self.in_row_owner_fld]
            where_clause = "1 = 1"
            in_row_nparr = self.convert_fc2np(self.in_row_features, row_fields, where_clause)

            if len(in_row_nparr) < 1:
                pimsilitool.AddWarning("No Right of Way features found!")

            # get engineering station network numpy array
            esn_fields = [self.in_eng_sta_network_unique_id, self.in_eng_sta_network_from_measure,
                          self.in_eng_sta_network_to_measure]
            where_clause = "1 = 1"
            self.in_esn_nparr = self.convert_fc2np(self.in_eng_sta_network_features, esn_fields, where_clause)

            if len(self.in_esn_nparr) < 1:
                pimsilitool.AddWarning("No Engineering Station Network features found!")
                return

            # get dig sheet crossing width
            if self.in_interrupt_crossing_width_source == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[1]:
                self.in_crossing_width = float(self.in_interrupt_crossing_width_value.split(" ")[0])
            else:
                self.in_crossing_width = 0

            # self.in_crossing_width = float(self.in_interrupt_crossing_width_value.split(" ")[0])
            #
            # if not self.in_crossing_width:
            #     self.in_crossing_width = 30

            # get dig sheet interruption features numpy array
            self.interrupt_nparr = self.get_dig_interrupt_nparray()

            ili_anomaly_measure_min = numpy.min(self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld])
            ili_anomaly_measure_max = numpy.max(self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld])

            weld_measure_min = numpy.min(in_weld_nparr[self.in_weld_measure_fld])
            weld_measure_max = numpy.max(in_weld_nparr[self.in_weld_measure_fld])
            self.dig_status_records = []
            self.anomaly_updates = []
            # get weld unique route ids
            weld_route_ids = numpy.unique(in_weld_nparr[self.in_weld_routeid_fld])
            for weld_route_id in weld_route_ids:
                pimsilitool.AddMessage("Processing route ID {}...".format(weld_route_id))
                isstart = True
                dig_from_meas = 0
                dig_to_meas = 0
                current_to_meas = 0
                target_anomalies_found = False
                isfirstweld = True

                weld_nparr = in_weld_nparr[in_weld_nparr[self.in_weld_routeid_fld] == weld_route_id]
                weld_nparr = numpy.sort(weld_nparr, order=[self.in_weld_measure_fld] )

                for i in range(0, len(weld_nparr)):
                    current_from_meas = weld_nparr[i][self.in_weld_measure_fld]
                    # check if there are anomalies between route strat measure and current_from_meas
                    # get route begin and end measures from engineesing station network
                    if isfirstweld:
                        esn_route = self.in_esn_nparr[self.in_esn_nparr[self.in_eng_sta_network_unique_id] == weld_route_id]
                        if len(esn_route) > 0:
                            dig_from_meas = esn_route[0][self.in_eng_sta_network_from_measure]
                        else:
                            dig_from_meas = 0
                        to_meas = current_from_meas
                        # check anomaly features between from and to measures
                        target_anomaly_features = self.get_target_anomalies_features(dig_from_meas, to_meas, weld_route_id, True)

                        if len(target_anomaly_features) > 0:
                            target_anomalies_found = True

                    else:
                        if i < (len(weld_nparr) - 1):
                            current_to_meas = weld_nparr[i + 1][self.in_weld_measure_fld]
                        else:
                            if current_to_meas < ili_anomaly_measure_max:
                                current_to_meas = ili_anomaly_measure_max
                            else:
                                continue

                        # check anomaly features between from and to measures
                        target_anomaly_features = self.get_target_anomalies_features(current_from_meas, current_to_meas, weld_route_id, True)

                        if len(target_anomaly_features) > 0:
                            target_anomalies_found = True
                            if isstart:
                                dig_from_meas = current_from_meas
                                isstart = False
                            to_meas = current_to_meas

                            # check anomalies for next weld
                            continue

                    # if len(anomaly_features) > 0:
                    if target_anomalies_found:
                        if isfirstweld:
                            isfirstweld = False
                            # get the closest weld
                            begin_weld_rec = self.get_closest_weld(weld_nparr, dig_from_meas)
                        else:
                            # get begin weld record
                            begin_weld_rec = weld_nparr[weld_nparr[self.in_weld_measure_fld] == dig_from_meas]
                            if len(begin_weld_rec) > 0:
                                begin_weld_rec = begin_weld_rec[0]

                        if len(begin_weld_rec) > 0:
                            begin_weld_routeid = begin_weld_rec[self.in_weld_routeid_fld]
                            begin_weld_id = begin_weld_rec[self.in_weldid_fld]
                            begin_weld_measure = begin_weld_rec[self.in_weld_measure_fld]
                        else:
                            begin_weld_rec = None
                            begin_weld_routeid = weld_route_id
                            begin_weld_id = "No Weld"
                            begin_weld_measure = to_meas

                        # get end weld record
                        end_weld_rec = self.get_anomaly_end_weld_record(weld_nparr, dig_from_meas, to_meas, True)
                        if end_weld_rec:
                            end_weld_routeid = end_weld_rec[self.in_weld_routeid_fld]
                            end_weld_id = end_weld_rec[self.in_weldid_fld]
                            end_weld_measure = end_weld_rec[self.in_weld_measure_fld]
                        else:
                            end_weld_routeid = weld_route_id
                            end_weld_id = "No Weld"
                            end_weld_measure = to_meas

                        # check if there are crossing features between from and to measures
                        crossing_features = self.get_crossing_features(dig_from_meas, end_weld_measure, begin_weld_routeid)
                        if len(crossing_features) > 0:  # crossibng features found
                            # get dig sheet crossing width
                            if self.in_interrupt_crossing_width_source == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[1]:
                                in_crossing_width = float(self.in_interrupt_crossing_width_value.split(" ")[0])
                            else:
                                in_crossing_width = crossing_features[0][self.in_interrupt_crossing_width_field]
                                if not in_crossing_width:
                                    in_crossing_width = 30

                            dn_crossing_measure = crossing_features[-1][self.in_interrupt_measure_fld] + (in_crossing_width / 2)
                            up_crossing_measure = crossing_features[0][self.in_interrupt_measure_fld] - (in_crossing_width / 2)

                            # check if anomalies found between dn_crossing_measure and up_crossing_measure
                            anomaly_features_up = self.get_target_anomalies_features(begin_weld_measure, up_crossing_measure, weld_route_id, True)

                            # check if anomalies found between dn_crossing_measure and up_crossing_measure
                            anomaly_features_on = self.get_target_anomalies_features(up_crossing_measure, dn_crossing_measure, weld_route_id, True)

                            # check if anomalies found between dn_crossing_measure and up_crossing_measure
                            anomaly_features_dn = self.get_target_anomalies_features(dn_crossing_measure, end_weld_measure, weld_route_id, True)

                            if len(anomaly_features_on) > 0: # anoumalies found in crossing features
                                # update anomalies dig id and create dig sheet feature between begin_weld_measure and end_weld_measure
                                anomalies = self.get_target_anomalies_features(dig_from_meas, end_weld_measure, weld_route_id, False)
                                dig_id = self.get_guid()
                                for anomaly in anomalies:
                                    id = anomaly[self.in_anomaly_id_fld]
                                    self.anomaly_updates.append((weld_route_id, id, dig_id))

                                # add dig sheet record with begin weld and end weld
                                self.add_dig_record_new(dig_id, dig_from_meas, end_weld_measure,
                                                        begin_weld_rec, end_weld_rec,
                                                        in_row_nparr, self.in_dig_reason_value,
                                                        self.in_dig_status_value,
                                                        self.in_dig_priority_value, self.in_dig_project_value, weld_route_id)

                            else:
                                if len(anomaly_features_up) > 0:  # anoumalies found between begin_weld_measure and up_crossing_measure

                                    # get begin weld ie upstream end weld from up_crossing_measure
                                    up_start_weld_rec = self.get_anomaly_end_weld_record(weld_nparr, up_crossing_measure, begin_weld_measure, False)

                                    if up_start_weld_rec:
                                        up_start_weld_measure = up_start_weld_rec[self.in_weld_measure_fld]
                                    else:
                                        up_start_weld_measure = begin_weld_measure

                                    # get closest weld to the up_crossing_measure
                                    up_end_weld_rec = self.get_closest_weld(weld_nparr, up_crossing_measure)

                                    # update anomalies dig id and create dig sheet feature between begin_weld_measure and up_crossing_measure
                                    anomalies = self.get_target_anomalies_features(up_start_weld_measure, up_crossing_measure, weld_route_id, False)
                                    dig_id = self.get_guid()
                                    for anomaly in anomalies:
                                        id = anomaly[self.in_anomaly_id_fld]
                                        self.anomaly_updates.append((weld_route_id, id, dig_id))

                                    # add dig sheet record with begin weld and end weld
                                    self.add_dig_record_new(dig_id, up_start_weld_measure, up_crossing_measure,
                                                            up_start_weld_rec, up_end_weld_rec,
                                                            in_row_nparr, self.in_dig_reason_value,
                                                            self.in_dig_status_value,
                                                            self.in_dig_priority_value, self.in_dig_project_value, weld_route_id)

                                if len(anomaly_features_dn) > 0:  # anoumalies found between dn_crossing_measure and end_weld_measure

                                    # get closest weld to the dn_crossing_measure
                                    dn_start_weld_rec = self.get_closest_weld(weld_nparr, dn_crossing_measure)

                                    # get end weld ie downstream end weld from dn_crossing_measure
                                    dn_end_weld_rec = self.get_anomaly_end_weld_record(weld_nparr, dn_crossing_measure, end_weld_measure, False)

                                    if dn_end_weld_rec:
                                        dn_end_weld_measure = dn_end_weld_rec[self.in_weld_measure_fld]
                                    else:
                                        dn_end_weld_measure = end_weld_measure

                                    # update anomalies dig id and create dig sheet feature between dn_crossing_measure and end_weld_measure
                                    anomalies = self.get_target_anomalies_features(dn_crossing_measure, dn_end_weld_measure, weld_route_id, False)
                                    dig_id = self.get_guid()
                                    for anomaly in anomalies:
                                        id = anomaly[self.in_anomaly_id_fld]
                                        self.anomaly_updates.append((weld_route_id, id, dig_id))

                                    # add dig sheet record with begin weld and end weld
                                    self.add_dig_record_new(dig_id, dn_crossing_measure, dn_end_weld_measure,
                                                            dn_start_weld_rec, dn_end_weld_rec,
                                                            in_row_nparr, self.in_dig_reason_value,
                                                            self.in_dig_status_value,
                                                            self.in_dig_priority_value, self.in_dig_project_value, weld_route_id)

                        else:
                            anomalies = self.get_target_anomalies_features(dig_from_meas, end_weld_measure, weld_route_id, False)
                            dig_id = self.get_guid()
                            for anomaly in anomalies:
                                id = anomaly[self.in_anomaly_id_fld]
                                self.anomaly_updates.append((weld_route_id, id, dig_id))

                            # add dig sheet record with begin weld and end weld
                            self.add_dig_record_new(dig_id, dig_from_meas, end_weld_measure, begin_weld_rec, end_weld_rec,
                                                in_row_nparr, self.in_dig_reason_value, self.in_dig_status_value,
                                                self.in_dig_priority_value, self.in_dig_project_value, weld_route_id)

                        isstart = True
                        target_anomalies_found = False

            if len(self.anomaly_updates) > 0:
                self.update_anomalies()
            else:
                pimsilitool.AddMessage("No anomalies found!")

            # populate dig sheet records
            if len(self.dig_status_records) > 0:
                self.insert_digsheet_recrods()
            else:
                pimsilitool.AddWarning("No Dig sheet records found!")
            return

        except Exception as e:
            tb = sys.exc_info()[2]
            pimsilitool.AddError("An error occurred on line %i" % tb.tb_lineno)
            pimsilitool.AddError(str(e))
            raise

    def update_anomaly_target_field(self):
        try:
            pimsilitool.AddMessage("Updating {} field...".format(self.in_anomaly_dig_target_fld))

            priority_values = []
            if self.in_anomaly_priority_values is not None:
                priority_values = self.in_anomaly_priority_values.split(";")

            with arcpy.da.UpdateCursor(self.in_anomaly_features,  field_names=[self.in_anomaly_priority_fld,
                                                self.in_anomaly_dig_target_fld, self.in_anomaly_digid_fld]) as cursor:
                for row in cursor:
                    row[1] = "No"
                    row[2] = None
                    if len(priority_values) > 0:
                        if row[0] and str(row[0]) in priority_values:
                            row[1] = "Yes"

                    cursor.updateRow(row)

        except Exception as e:
            raise

    def convert_fc2np(self, in_layer, flds, where_clause):
        try:

            np_arr = []
            if arcpy.Exists(in_layer):
                np_arr = arcpy.da.FeatureClassToNumPyArray(in_layer, flds, where_clause, null_value=-9999)
            return np_arr
        except Exception as e:
            raise

    def add_dig_record(self, routeid, from_meas, to_meas, dig_id, begin_weld_rec, end_weld_rec, row_rec, in_dig_reason_value,
                       in_dig_status_value, in_dig_priority_value, in_dig_project_value, first_anomaly_measure,
                       last_anomaly_measure, weld_nparr):

        try:

            if len(row_rec) > 0:
                row_owner_id = row_rec[0][self.in_row_owner_fld]
            else:
                row_owner_id = None
            begin_weld_id = begin_weld_rec[0][self.in_weldid_fld]


            # check if dig interruption features found between from and to measures
            interrupt_features = []
            if len(self.interrupt_nparr) > 0:
                interrupt_features = self.interrupt_nparr[
                                                (self.interrupt_nparr[self.in_interrupt_measure_fld] > from_meas) &
                                                (self.interrupt_nparr[self.in_interrupt_measure_fld] < to_meas) &
                                                (self.interrupt_nparr[self.in_interrupt_routeid_fld] == routeid)
                                                ]
            interrupt_feature = []
            if len(interrupt_features) > 0:
                pimsilitool.AddMessage(interrupt_features)
                # get the upstream interrupt features measure
                interrupt_feature = numpy.sort(interrupt_features, order=self.in_interrupt_measure_fld)

            # if len(interrupt_feature) > 0:   # get the upstream and downstream welds
                dn_interrupt_pointm = interrupt_feature[-1][self.in_interrupt_measure_fld]
                up_interrupt_pointm = interrupt_feature[0][self.in_interrupt_measure_fld]
                # get dig sheet crossing width
                if self.in_interrupt_crossing_width_source == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[1]:
                    in_crossing_width = float(self.in_interrupt_crossing_width_value.split(" ")[0])
                else:
                    in_crossing_width = interrupt_feature[0][self.in_interrupt_crossing_width_field]
                    if not in_crossing_width:
                        in_crossing_width = 30
                min_dig_distance = in_crossing_width / 2
                dn_min_from_measure = dn_interrupt_pointm + min_dig_distance  # from measure for downstream weld

                # get downstream end weld record
                dn_end_weld_rec =  self.get_anomaly_end_weld_record(weld_nparr, dn_min_from_measure, dn_min_from_measure, True)
                if len(dn_end_weld_rec) > 0:

                    end_weld_routeid = end_weld_rec[0][self.in_weld_routeid_fld]
                    end_weld_id = end_weld_rec[0][self.in_weldid_fld]
                    # end_pointx = end_weld_rec[0]["SHAPE@X"]
                    # end_pointy = end_weld_rec[0]["SHAPE@Y"]
                    # end_pointm = end_weld_rec[0][self.in_weld_measure_fld]

                    dn_end_weld_measure = dn_end_weld_rec[0][self.in_weld_measure_fld]
                    dn_shape = self.get_digsheet_shape_new(dn_min_from_measure, dn_end_weld_measure, routeid)
                    if dn_shape:
                        dn_first_point_x = dn_shape.firstPoint.X
                        dn_first_point_y = dn_shape.firstPoint.Y
                        dn_last_point_x = dn_shape.lastPoint.X
                        dn_last_point_y = dn_shape.lastPoint.Y
                        self.dig_status_records.append((dn_shape,
                                                        routeid, dn_min_from_measure, end_weld_routeid, dn_end_weld_measure,
                                                        dig_id,
                                                        begin_weld_id, # TODO get begin weld id
                                                        dn_min_from_measure, end_weld_id,  dn_end_weld_measure,
                                                        row_owner_id, in_dig_reason_value, in_dig_status_value,
                                                        in_dig_priority_value, in_dig_project_value,
                                                        dn_first_point_x, dn_first_point_y, dn_last_point_x, dn_last_point_y)
                                                       )

                # get upstream start weld record
                up_min_to_measure = up_interrupt_pointm - min_dig_distance  # to measure for upstream weld
                up_start_weld_rec = self.get_anomaly_end_weld_record(weld_nparr, up_min_to_measure, up_min_to_measure, False)
                if len(up_start_weld_rec) > 0:
                    begin_weld_id = begin_weld_rec[-1][self.in_weldid_fld]

                    begin_weld_routeid = begin_weld_rec[-1][self.in_weld_routeid_fld]
                    # begin_pointx = begin_weld_rec[0]["SHAPE@X"]
                    # begin_pointy = begin_weld_rec[0]["SHAPE@Y"]
                    # begin_pointm = from_meas

                    up_start_weld_measure = up_start_weld_rec[-1][self.in_weld_measure_fld]
                    up_shape = self.get_digsheet_shape_new(up_start_weld_measure, up_min_to_measure, routeid)
                    if up_shape:
                        up_first_point_x = up_shape.firstPoint.X
                        up_first_point_y = up_shape.firstPoint.Y
                        up_last_point_x = up_shape.lastPoint.X
                        up_last_point_y = up_shape.lastPoint.Y
                        self.dig_status_records.append((up_shape,
                                                        begin_weld_routeid, up_start_weld_measure, routeid, up_min_to_measure,
                                                        dig_id,
                                                        begin_weld_id, up_start_weld_measure,
                                                        end_weld_id,    # TODO get end weld id
                                                        up_min_to_measure,
                                                        row_owner_id, in_dig_reason_value, in_dig_status_value,
                                                        in_dig_priority_value, in_dig_project_value,
                                                        up_first_point_x, up_first_point_y, up_last_point_x, up_last_point_y)
                                                       )

            else:
                begin_weld_id = begin_weld_rec[0][self.in_weldid_fld]
                begin_weld_measure = begin_weld_rec[0][self.in_weld_measure_fld]
                begin_weld_routeid = begin_weld_rec[0][self.in_weld_routeid_fld]
                begin_pointx = begin_weld_rec[0]["SHAPE@X"]
                begin_pointy = begin_weld_rec[0]["SHAPE@Y"]
                begin_pointm = from_meas

                begin_point = arcpy.Point(begin_pointx, begin_pointy, 0, begin_pointm)

                # check if there are dig interruption features between first anomanly measure and downstream weld measure
                if len(end_weld_rec) > 0:
                    end_weld_measure = end_weld_rec[0][self.in_weld_measure_fld]
                    end_weld_routeid = end_weld_rec[0][self.in_weld_routeid_fld]
                    end_weld_id = end_weld_rec[0][self.in_weldid_fld]
                    end_pointx = end_weld_rec[0]["SHAPE@X"]
                    end_pointy = end_weld_rec[0]["SHAPE@Y"]
                    end_pointm = end_weld_rec[0][self.in_weld_measure_fld]

                else:
                    end_pointx = None
                    end_pointy = None
                    end_pointm = None
                    end_weld_id = None
                    end_weld_measure = None
                    end_weld_routeid = None

                end_point = arcpy.Point(end_pointx, end_pointy, 0, end_pointm)

                pl_shape = self.get_digsheet_shape(begin_pointm, end_pointm, routeid, begin_point, end_point)

                if pl_shape is not None:
                    # self.dig_status_records.append((pointx, pointy, 0, pointm,
                    self.dig_status_records.append((pl_shape,
                                                    begin_weld_routeid, begin_pointm, end_weld_routeid, end_pointm, dig_id,
                                                    begin_weld_id, begin_weld_measure, end_weld_id, end_weld_measure,
                                                    row_owner_id, in_dig_reason_value, in_dig_status_value,
                                                    in_dig_priority_value, in_dig_project_value,
                                                    begin_pointx, begin_pointy, end_pointx, end_pointy)
                                                   )
        except Exception as e:
            raise

    def get_digsheet_shape_new(self, weld_from_meas, weld_end_meas, routeid):
        try:
            pimsilitool.AddMessage( "(New) Extracting polyline segment between measures {} and {}...".format(weld_from_meas, weld_end_meas))

            if weld_end_meas is None or len(self.in_esn_nparr) < 1:
                pimsilitool.AddWarning("Weld end measure/engineering station network feature error for route id: {}".format(routeid))
                return None

            where = "{} = '{}'".format(self.in_eng_sta_network_unique_id, routeid)
            line_seg = None
            with arcpy.da.SearchCursor(self.in_eng_sta_network_features,
                                   [self.in_eng_sta_network_from_measure, self.in_eng_sta_network_to_measure, "SHAPE@"],
                                   where_clause=where) as cursor:
                for row in cursor:
                    from_meas = row[0]
                    to_meas = row[1]
                    esn_shape = row[2]

                    from_pct = weld_from_meas / (to_meas - from_meas)
                    to_pct =  weld_end_meas / (to_meas - from_meas)

                    # query = esn_shape.queryPointAndDistance(point)
                    # query1 = esn_shape.queryPointAndDistance(point1)

                    line_seg = esn_shape.segmentAlongLine(from_pct, to_pct, True)
                    break
            pimsilitool.AddMessage(line_seg)
            return line_seg

        except Exception as e:
            raise

    def get_digsheet_shape(self, weld_from_meas, weld_end_meas, routeid, point, point1):
        try:
            pimsilitool.AddMessage("Extracting polyline segment between measures {} and {}...".format(weld_from_meas, weld_end_meas))

            if weld_end_meas is None or len(self.in_esn_nparr) < 1:
                pimsilitool.AddWarning("Weld end measure/engineering station network feature error for route id: {}".format(routeid))
                return None

            where = "{} = '{}'".format(self.in_eng_sta_network_unique_id, routeid)
            line_seg = None
            with arcpy.da.SearchCursor(self.in_eng_sta_network_features,
                                             [self.in_eng_sta_network_from_measure, self.in_eng_sta_network_to_measure, "SHAPE@"],
                                             where_clause = where) as cursor:
                for row in cursor:
                    esn_shape = row[2]

                    query = esn_shape.queryPointAndDistance(point)
                    query1 = esn_shape.queryPointAndDistance(point1)

                    line_seg = esn_shape.segmentAlongLine(query[1], query1[1])
                    break
            pimsilitool.AddMessage(line_seg)
            return line_seg

        except Exception as e:
            raise

    def insert_digsheet_recrods(self):
        try:
            pimsilitool.AddMessage("Inserting dig sheet records...")

            flds = ["DIG_ID", "BEGIN_MEASURE", "END_MEASURE", "BEGIN_WELD_ROUTE_ID", "BEGIN_WELD_ID", "BEGIN_WELD_MEASURE",
                    "END_WELD_ROUTE_ID", "END_WELD_ID", "END_WELD_MEASURE", "LAND_OWNER",
                    "DIG_REASON", "DIG_STATUS", "DIG_PRIORITY", "DIG_PROJECT"]

            with arcpy.da.InsertCursor(self.events_table, flds) as cursor:
                for row in self.dig_status_records:
                    cursor.insertRow(row)

            pipe_excavation_events =  "PIPE_EXCAVATION_Events1"
            if arcpy.Exists(pipe_excavation_events):
                arcpy.Delete_management(pipe_excavation_events)
            out_pipe_excavation_events = "PIPE_EXCAVATION_EVENTS_FC"
            arcpy.MakeRouteEventLayer_lr(self.in_eng_sta_network_features, self.in_eng_sta_network_unique_id,
                                         self.events_table,
                                         "BEGIN_WELD_ROUTE_ID; Line; BEGIN_MEASURE; END_MEASURE", pipe_excavation_events, None,
                                         "NO_ERROR_FIELD", "NO_ANGLE_FIELD", "NORMAL", "ANGLE", "LEFT", "POINT")

            flds = ["SHAPE@",
                    self.in_digsheet_begin_routeid_field, self.in_digsheet_begin_measure_field,
                    self.in_digsheet_end_routeid_field, self.in_digsheet_end_measure_field,
                    self.in_dig_id_fld,
                    self.in_dig_begin_weldid_fld, self.in_dig_begin_weld_measure_fld,
                    self.in_dig_end_weldid_fld, self.in_dig_end_weld_measure_fld, self.in_dig_row_owner_fld,
                    self.in_dig_reason_fld, self.in_dig_status_fld, self.in_dig_priority_fld,
                    self.in_dig_project_fld,
                    self.in_digsheet_begin_exc_long_field, self.in_digsheet_begin_exc_lat_field,
                    self.in_digsheet_end_exc_long_field, self.in_digsheet_end_exc_lat_field
                    ]
            events_flds = ["SHAPE@",
                           "BEGIN_WELD_ROUTE_ID", "BEGIN_MEASURE",
                           "END_WELD_ROUTE_ID","END_MEASURE",
                           "DIG_ID",
                           "BEGIN_WELD_ID","BEGIN_WELD_MEASURE",
                           "END_WELD_ID", "END_WELD_MEASURE", "LAND_OWNER",
                           "DIG_REASON", "DIG_STATUS", "DIG_PRIORITY",
                           "DIG_PROJECT" ]


            with arcpy.da.InsertCursor(self.in_dig_features, flds) as cursor:
                with arcpy.da.SearchCursor(pipe_excavation_events, events_flds) as eve_cursor:
                    for eve_row in eve_cursor:
                        row = (eve_row[0],
                             eve_row[1],
                             eve_row[2],
                             eve_row[3],
                             eve_row[4],
                             eve_row[5],
                             eve_row[6],
                             eve_row[7],
                             eve_row[8],
                             eve_row[9],
                             eve_row[10],
                             eve_row[11],
                             eve_row[12],
                             eve_row[13],
                             eve_row[14],
                             eve_row[0].firstPoint.X,
                             eve_row[0].firstPoint.Y,
                             eve_row[0].lastPoint.X,
                             eve_row[0].lastPoint.Y
                             )
                        cursor.insertRow(row)

        except Exception as e:
            raise

    def get_guid(self):
        return '{' + str(uuid.uuid4()) + '}'

    def get_anomaly_end_weld_record(self, weld_nparr, from_meas, to_meas, is_dnstream):
        try:
            end_weld_rec = None
            dist_between_welds = abs(from_meas - to_meas)

            if is_dnstream:
                if dist_between_welds < self.in_min_dig_length:
                    weld_dist = from_meas + self.in_min_dig_length
                else:
                    weld_dist = to_meas
                end_weld_rec = weld_nparr[weld_nparr[self.in_weld_measure_fld] >= weld_dist]

                # if there are no welds at self.in_min_dig_length, get the last weld
                if len(end_weld_rec) < 1:
                    end_weld_rec = weld_nparr[weld_nparr[self.in_weld_measure_fld] >= from_meas]

                if len(end_weld_rec) > 1:
                    end_weld_rec = end_weld_rec[0]

            else:
                if dist_between_welds < self.in_min_dig_length:
                    weld_dist = from_meas - self.in_min_dig_length
                else:
                    weld_dist = to_meas
                end_weld_rec = weld_nparr[weld_nparr[self.in_weld_measure_fld] <= weld_dist]

                # if there are no welds at self.in_min_dig_length, get the last weld
                if len(end_weld_rec) < 1:
                    end_weld_rec = weld_nparr[weld_nparr[self.in_weld_measure_fld] <= from_meas]

                if len(end_weld_rec) > 1:
                    end_weld_rec = end_weld_rec[-1]

            return end_weld_rec

        except Exception as e:
            raise

    def get_dig_interrupt_nparray(self):
        try:
            interrupt_nparr = []

            if self.in_interrupt_features is not None:
                interrupt_layers = self.in_interrupt_features.split(";")

                where_clause = "1 = 1"

                for layer in interrupt_layers:
                    if not arcpy.Exists(layer):
                        continue

                    # check if input fields exists in the feature class
                    in_flds = []
                    in_flds += [f.name.upper() for f in arcpy.ListFields(layer)]

                    if self.in_interrupt_crossing_width_source == config.DIGSHEET_LAYOUT_CROSSING_WIDTH_SOURCE[0]:
                        check_flds = [self.in_interrupt_routeid_fld, self.in_interrupt_id_fld,
                                      self.in_interrupt_measure_fld, self.in_interrupt_crossing_width_field]
                        interrupt_fields = [self.in_interrupt_routeid_fld, self.in_interrupt_id_fld,
                                            self.in_interrupt_measure_fld, "SHAPE@X", "SHAPE@Y",  self.in_interrupt_crossing_width_field]
                    else:
                        check_flds = [self.in_interrupt_routeid_fld, self.in_interrupt_id_fld, self.in_interrupt_measure_fld]
                        interrupt_fields = [self.in_interrupt_routeid_fld, self.in_interrupt_id_fld,
                                            self.in_interrupt_measure_fld, "SHAPE@X", "SHAPE@Y"]

                    fld_exists = True
                    for fld in check_flds:
                        if fld.upper() not in in_flds:
                            pimsilitool.AddWarning("Feature class {} has no field {}, skipping this feature class!".format(layer, fld))
                            fld_exists = False

                    if fld_exists:
                        # check layer geometry type, if polyline then intersect analysis
                        # with engineering station network to create intersection points
                        shape_type = arcpy.Describe(layer).shapeType
                        out_point_layer = os.path.join(arcpy.env.scratchGDB, "ESN_Layer_Intersect")
                        if shape_type == "Polyline":
                            arcpy.Intersect_analysis([layer, self.in_eng_sta_network_features], out_point_layer, "", "", "POINT")
                        if arcpy.Exists(out_point_layer) and int(
                                arcpy.GetCount_management(out_point_layer).getOutput(0)) > 0:
                            nparr = self.convert_fc2np(out_point_layer, interrupt_fields, where_clause)
                        else:
                            nparr = self.convert_fc2np(layer, interrupt_fields, where_clause)

                        if len(nparr) > 0:
                            if len(interrupt_nparr) < 1:
                                interrupt_nparr = nparr
                            else:
                                interrupt_nparr = numpy.append(interrupt_nparr, nparr)

            if len(interrupt_nparr) > 0:
                numpy.sort(interrupt_nparr, order=self.in_interrupt_measure_fld)

            return interrupt_nparr

        except Exception as e:
            raise

    def get_crossing_features(self, from_meas, to_meas, route_id):
        try:
            crossing_features = []
            if len(self.interrupt_nparr) > 0:
                crossing_features = self.interrupt_nparr[
                                                    (self.interrupt_nparr[self.in_interrupt_measure_fld] > from_meas) &
                                                    (self.interrupt_nparr[self.in_interrupt_measure_fld] < to_meas) &
                                                    (self.interrupt_nparr[self.in_interrupt_routeid_fld] == route_id)
                                                    ]
            return crossing_features

        except Exception as e:
            raise

    def get_target_anomalies_features(self, from_meas, to_meas, route_id, istarget):
        try:
            anomaly_features = []
            if istarget:

                anomaly_features = self.in_ili_anomaly_nparr[
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] >= from_meas) &
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] <= to_meas) &
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_dig_target_fld] == "Yes") &
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_routeid_fld] == route_id)
                                        ]
            else:
                anomaly_features = self.in_ili_anomaly_nparr[
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] >= from_meas) &
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] <= to_meas) &
                                        (self.in_ili_anomaly_nparr[self.in_anomaly_routeid_fld] == route_id)
                                        ]

            return anomaly_features

        except Exception as e:
            raise

    def get_anomalies_features(self, from_meas, to_meas, route_id):
        try:
            anomaly_features = []

            anomaly_features = self.in_ili_anomaly_nparr[
                                    (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] >= from_meas) &
                                    (self.in_ili_anomaly_nparr[self.in_anomaly_measure_fld] <= to_meas) &
                                    (self.in_ili_anomaly_nparr[self.in_anomaly_routeid_fld] == route_id)
                                    ]


            return anomaly_features

        except Exception as e:
            raise

    def get_closest_weld(self, weld_nparr, in_meas):
        try:
            # check if there is weld at the measure
            weld_rec = None
            weld_recs = weld_nparr[weld_nparr[self.in_weld_measure_fld] == in_meas]
            if len(weld_recs) > 0:
                weld_rec = weld_rec[0]
            else:
                weld_recs_up = weld_nparr[weld_nparr[self.in_weld_measure_fld] < in_meas]
                weld_recs_dn = weld_nparr[weld_nparr[self.in_weld_measure_fld] > in_meas]
                dn_weld_meas = None
                up_weld_meas = None
                if len(weld_recs_up) > 0:
                    up_weld_meas = weld_recs_up[-1][self.in_weld_measure_fld]
                if len(weld_recs_dn) > 0:
                    dn_weld_meas = weld_recs_dn[0][self.in_weld_measure_fld]
                if up_weld_meas is None:
                    if dn_weld_meas is not None:
                        weld_rec = weld_recs_dn[0]
                elif up_weld_meas is None:
                    if up_weld_meas is not None:
                        weld_rec = weld_recs_up[-1]
                else:
                    if up_weld_meas < dn_weld_meas:
                        weld_rec = weld_recs_up[-1]
                    else:
                        weld_rec = weld_recs_dn[0]
            return weld_rec

        except Exception as e:
            raise

    def get_right_of_way_owner(self, in_row_nparr, from_meas, to_meas):
        try:
            row_owner_id = None
            if len(in_row_nparr) > 0:
                row_recs = in_row_nparr[
                                        (in_row_nparr[self.in_row_end_measure_fld] >= from_meas) &
                                        (in_row_nparr[self.in_row_begin_measure_fld] <= to_meas)
                                        ]
            else:
                row_recs = []

            if len(row_recs) > 0:
                owners = "; ".join(str(x) for x in set(row_recs[self.in_row_owner_fld]) if x is not None)
                row_owner_id = owners

            return row_owner_id

        except Exception as e:
                raise

    def add_dig_record_new(self, dig_id, begin_measure, end_measure, begin_weld_rec, end_weld_rec,
                in_row_nparr, in_dig_reason_value, in_dig_status_value, in_dig_priority_value, in_dig_project_value, weld_route_id):
        try:
            row_owner_id = self.get_right_of_way_owner(in_row_nparr, begin_measure, end_measure)
            if begin_weld_rec:
                begin_weld_routeid = begin_weld_rec[self.in_weld_routeid_fld]
                begin_weld_id = begin_weld_rec[self.in_weldid_fld]
                begin_weld_measure = begin_weld_rec[self.in_weld_measure_fld]
            else:
                begin_weld_routeid = weld_route_id
                begin_weld_id = None
                begin_weld_measure = begin_measure

            if end_weld_rec:
                end_weld_routeid = end_weld_rec[self.in_weld_routeid_fld]
                end_weld_id = end_weld_rec[self.in_weldid_fld]
                end_weld_measure = end_weld_rec[self.in_weld_measure_fld]
            else:
                end_weld_routeid = weld_route_id
                end_weld_id = None
                end_weld_measure = end_measure
            self.dig_status_records.append((dig_id, begin_measure, end_measure,
                                            begin_weld_routeid, begin_weld_id, begin_weld_measure,
                                            end_weld_routeid, end_weld_id, end_weld_measure,
                                            row_owner_id, in_dig_reason_value,
                                            in_dig_status_value, in_dig_priority_value, in_dig_project_value))
        except Exception as e:
                raise

    def create_dig_sheet_events_table(self):
        try:
            events_table_name = "Dig_Sheet_Events"
            self.events_table = os.path.join(arcpy.env.scratchGDB, events_table_name)
            if arcpy.Exists(self.events_table):
                arcpy.Delete_management(self.events_table)
            EVENTS_TABLE_FIELD_DESCRIPTION = [["DIG_ID", "TEXT", "DIG_ID", 60],
                                                ["BEGIN_MEASURE", "DOUBLE", "BEGIN_MEASURE", None],
                                                ["END_MEASURE", "DOUBLE", "END_MEASURE", None],
                                                ["BEGIN_WELD_ROUTE_ID", "TEXT", "BEGIN_WELD_ROUET_ID", 60],
                                                ["BEGIN_WELD_ID", "TEXT", "BEGIN_WELD_ID", 60],
                                                ["BEGIN_WELD_MEASURE", "DOUBLE", "BEGIN_WELD_MEASURE", None],
                                                ["END_WELD_ROUTE_ID", "TEXT", "END_WELD_ROUET_ID", 60],
                                                ["END_WELD_ID", "TEXT", "END_WELD_ID", 60],
                                                ["END_WELD_MEASURE", "DOUBLE", "END_WELD_MEASURE", None],
                                                ["LAND_OWNER", "TEXT", "LAND_OWNER", 255],
                                                ["DIG_REASON", "TEXT", "DIG_REASON", 255],
                                                ["DIG_STATUS", "TEXT", "DIG_STATUS", 255],
                                                ["DIG_PRIORITY", "TEXT", "DIG_PRIORITY", 255],
                                                ["DIG_PROJECT", "TEXT", "DIG_PROJECT", 255]
                                              ]
            arcpy.CreateTable_management(arcpy.env.scratchGDB, events_table_name)
            arcpy.AddFields_management(self.events_table, EVENTS_TABLE_FIELD_DESCRIPTION)

        except Exception as e:
            raise

    def update_anomalies(self):
        try:
            with arcpy.da.UpdateCursor(self.in_anomaly_features,
                                   field_names = [self.in_anomaly_digid_fld, self.in_anomaly_routeid_fld,
                                                  self.in_anomaly_id_fld] ) as cursor:
                for row in cursor:

                    # get dig id from self.anonaky_updates
                    for anomaly in self.anomaly_updates:
                        if anomaly[0] and anomaly[1]:
                            if str(anomaly[0]) == str(row[1]) and str(anomaly[1]) == str(row[2]):
                                row[0] = anomaly[2]
                                cursor.updateRow(row)

        except Exception as e:
            raise
