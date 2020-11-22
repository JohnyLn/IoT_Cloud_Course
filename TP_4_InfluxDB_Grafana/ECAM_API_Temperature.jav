flowFile = session.get();
if (flowFile != null) {
    var StreamCallback = Java.type("org.apache.nifi.processor.io.StreamCallback");
    var IOUtils = Java.type("org.apache.commons.io.IOUtils");
    var StandardCharsets = Java.type("java.nio.charset.StandardCharsets");
    var error = false;
    var measure = "paris_weather"
    var line = "";
    var sep = "\n"

    // Get attributes
    flowFile = session.write(flowFile, new StreamCallback(function (inputStream, outputStream) {
        var content = IOUtils.toString(inputStream, StandardCharsets.UTF_8); // message or content
        var message_content = {};
        var city = "";
        var date = "";
        var temp = "";
        var pres = "";
        var humi = "";

        try {
            message_content = JSON.parse(content);
            for (key in message_content) {
                if (key == 'city') {
                    city = message_content[key]
                } else if (key == 'date') {
                    date = message_content[key]
                } else if (key == 'temp') {
                    temp = message_content[key]
                } else if (key == 'pressure') {
                    pres = message_content[key]
                }
                else if (key == 'humidity') {
                    humi = message_content[key]
                }
            }
            line = measure + " " + "temperature" + "=" + temp+ " " + sep

            // Write output content
            outputStream.write(line.getBytes(StandardCharsets.UTF_8));

        } catch (e) {
            error = true;
            log.error('Something went wrong', e)
            outputStream.write(content.getBytes(StandardCharsets.UTF_8));
        }
    }));

    if (error) {
        session.transfer(flowFile, REL_FAILURE)
    } else {
        session.transfer(flowFile, REL_SUCCESS)
    }
}