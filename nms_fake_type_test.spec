/*
A KBase module: nms_fake_type_test
*/

module nms_fake_type_test {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_nms_fake_type_test(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
