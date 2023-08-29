<!DOCTYPE html>
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="/static/js.js"></script>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>

         
        <form  id="myform">
            <div class="two-col">
                <label for="init_network" class="cell">Initial Network Address</label>
                <label for="init_slash" class="cell">Slash Notation</label>
                <input type="text" class="cell" name="init_network" id="init_network" value="192.168.1.0">
                <input type="number" class="cell" min="1" max="32" name="init_slash" value="24">

            </div>

            <div>
                <div id="subnet">
                    <label for="sub_name" class="cell">Subnet Name</label>
                    
                    <label for="sub_size" class="cell">Subnet Size</label>
                    <input type="text" name="sub_name-0" id="sub_name" class="cell" value="A">
                    <input type="text" name="sub_size-0" id="sub_size" class="cell" value="20">
                </div>
                <div>
                    <input type="number" min='1' max='25' id='rows' value="1" >
                    <input type="button" id="add_rows" value="Add New Subnet" class="bt">
                </div>
            </div>
            <div>
                <input type="submit" id='sub' vlaue="Submit" class="bt">
            </div>
        </form>
        <div id="result"></div>
        
    <body>
</html>

