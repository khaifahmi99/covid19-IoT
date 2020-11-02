var AWS = require('aws-sdk');
AWS.config.update({ region: 'ap-southeast-2' });
var docClient = new AWS.DynamoDB.DocumentClient({ apiVersion: '2012-08-10' });
exports.handler = async(event) => {
    try {

        var queryString = event["queryStringParameters"];
        if (queryString == null) {
            return {
                statusCode: 400,
                body: "Missing parameters",
            }
        }

        var triggerType = queryString["triggerType"];

        if (triggerType == null || isNullOrWhitespace(triggerType)) {
            return {
                statusCode: 400,
                body: "Missing parameter : triggerType",
            }
        }

        if (triggerType.toLowerCase() == "all") {
            
             var params = {
                TableName: 'CameraData',
            };

            console.log("Getting data from dynamodb by triggerType: " + triggerType);

            const data = await docClient.scan(params).promise();

            return {
                statusCode: 200,
                headers: {
                    "Access-Control-Allow-Headers": "*",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*"
                },
                body: JSON.stringify(data.Items),
            };
        }
        else {
            var params = {
                TableName: 'CameraData',
                IndexName: 'TriggerType-index',
                KeyConditionExpression: 'TriggerType = :triggerType',
                ExpressionAttributeValues: {
                    ':triggerType': triggerType,
                }
            };

        }


        console.log("Getting data from dynamodb by triggerType: " + triggerType);

        const data = await docClient.query(params).promise();

        return {
            statusCode: 200,
            headers: {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            },
            body: JSON.stringify(data.Items),
        };
    }
    catch (e) {

        console.log("error")

        return {
            statusCode: 500,
            body: e.message,
        };
    }
};

function isNullOrWhitespace(input) {

    if (typeof input === 'undefined' || input == null) return true;

    return input.replace(/\s/g, '').length < 1;
}
