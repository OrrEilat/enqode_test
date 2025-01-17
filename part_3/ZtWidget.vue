<script setup>

// the data prop contains the json data for the widget
const { data } = defineProps({
    data: Object,
});

// determines the display color based on the risk category
// input: the json data
// output: a processed data object
function process_data(d) {

    let riskCategory = d.riskCategory;
    let riskColor = "green";
    if (riskCategory === "Moderate Risk") {
        riskColor = "orange";
    } else if (riskCategory === "High Risk") {
        riskColor = "red";
    }

    return {
        name: d.companyName,
        zeroTrustScore: d.zeroTrustScore,
        riskCategory: riskCategory,
        riskColor: riskColor,
        metrics: d.metrics,
    };
}

// produces a description for a metric
// the description is based on the metric name and the metric value
// currently, the description is a placeholder
// input: the metric name and the metric value
// output: a string description
function get_metric_description(metric_name, metric_value) {
    let metric_description = "";

    if (metric_value < 34) {
        metric_description += "Metric is low risk.";
    } else if (metric_value >= 34 && metric_value < 67) {
        metric_description += "Metric is moderate risk.";
    } else if (metric_value >= 67) {
        metric_description += "Metric is high risk.";
    }

    metric_description += "<br>";

    switch (metric_name) {
        case "metric1":
            metric_description += "Description for metric 1.";
            break;
        case "metric2":
            metric_description += "Description for metric 2.";
            break;
        case "metric3":
            metric_description += "Description for metric 3.";
            break;
    }
    return metric_description;
}

// the processed data object
const p_data = process_data(data);

</script>

<template >
    <v-card theme="dark mb-2">
        <v-container >
            
            <!-- company name and risk category -->
            <v-row>
                <v-col>
                    <h1>{{p_data.name}}</h1>
                </v-col>
                <v-col cols="3">
                    <v-card
                        :color="p_data.riskColor"
                        text-color="white"
                        style="height:40px; width:120px"
                        class="text-center font-weight-bold"
                    >
                        {{p_data.riskCategory}}
                    </v-card>
                </v-col>
                <v-col>

                </v-col>
            </v-row>

            <!-- zero trust score -->
            <v-row>
                <v-col cols="3">
                    <p class="font-weight-bold" style="width:400px">Zero Trust Score:</p>
                </v-col>
                <v-col>
                    <v-progress-linear
                        :color="p_data.riskColor"
                        :model-value="p_data.zeroTrustScore"
                        height="30"
                    >{{p_data.zeroTrustScore}}</v-progress-linear>
                </v-col>
            </v-row>

            <!-- metrics -->
            <v-row v-for="(value, key) in p_data.metrics" :key="key">
                <v-divider></v-divider>
                <v-col cols="4">
                    <p class="font-weight-bold">{{key}}</p>
                    <p 
                    v-html="get_metric_description(key, value)"
                    style="color:lightgrey"
                    ></p>
                </v-col>
                <v-col>
                    <v-progress-linear
                        color="blue"
                        :model-value="value"
                        height="20"
                    >{{value}}</v-progress-linear>
                </v-col>
            </v-row>
        
        </v-container>
    </v-card>
</template>