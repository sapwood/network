<!DOCTYPE html>
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="/static/js.js"></script>
    </head>
    <body>

         
        <form  id="myform">
            <div>
                <label for="init_network">Initial Network Address</label>
                <input type="text" name="init_network" id="init_network" placeholder="192.168.1.0">
                <input type="number" min="1" max="32" name="init_slash" placeholder="24">
            </div>
            <div>
                <label for="subnet_amount">Number of subnets:</label>
                <input type="number" min="2" max="30" name="subnet_amount" id="subnet_amount" placeholder="2">
            </div>
            <div>
                <div id="subnet">
                    <label for="sub_name">Subnet Name</label>
                    <input type="text" name="sub_name" id="sub_name" placeholder="A">
                    <label for="sub_size">Subnet Size</label>
                    <input type="text" name="sub_size" id="sub_size">
                </div>
                <div>
                    <input type="number" min='1' max='30' id='rows' placeholder="1">
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

