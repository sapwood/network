<!DOCTYPE html>
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="/static/js.js"></script>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>

         
        <form  id="myform">
            <div>
                <label for="init_network">Initial Network Address</label>
                <input type="text" name="init_network" id="init_network" value="192.168.1.0">
                <input type="number" min="1" max="32" name="init_slash" value="24">
            </div>

            <div>
                <div id="subnet">
                    <label for="sub_name">Subnet Name</label>
                    <input type="text" name="sub_name-0" id="sub_name" value="A">
                    <label for="sub_size">Subnet Size</label>
                    <input type="text" name="sub_size-0" id="sub_size" value="20">
                </div>
                <div>
                    <input type="number" min='1' max='30' id='rows' value="1">
                    <input type="button" id="add_rows" value="Add">
                </div>
            </div>
            <div>
                <input type="submit" id='sub' vlaue="Submit">
            </div>
        </form>
        <div id="result"></div>
        
    <body>
</html>

