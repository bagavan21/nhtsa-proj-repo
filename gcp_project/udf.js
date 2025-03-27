    
    
    
    
    function transform(line) {
    var values = line.split(',');
    
    var obj = new Object();
    obj.name = values[0];
    obj.city = values[1];
    obj.country = values[2];
    var jsonString = JSON.stringify(obj);

    return jsonString;
    }