$("document").ready(function(){

            function blue_and_copy(){
                $("td#copy_to_clipboard").mouseover(function(){
                    $(this).css({"color":"#1E90FF", "cursor":"pointer"});
                    $(this).children().css({"visibility":"visible", "margin-top":"25px", "margin-left":"50px", "padding-left":"2px", "padding-right":"2px","border":"1px solid black", "background-color":"#F0E68C", "color":"black","font-size":"4px"});
                });

                $("td#copy_to_clipboard").mouseout(function(){
                    $(this).css({"color":"#808080"});
                    $(this).children().css({"visibility":"hidden"});
                });

                $("td#copy_to_clipboard").dblclick(function(){
                    $(this).select();
                    document.execCommand('copy');

                });
            }

            function ajax_all_boss(){
                $.getJSON('/ajax_all_boss/', function(ret){
                    $("#all_boss").empty();
                    $("#all_boss").append("<tr><th>Boss</th><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var boss = ret[i].split(",")[0];
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#all_boss').append("<tr><td>" + boss + "</td><td>" + level +
                        '</td><td id="copy_to_clipboard" style="color:#808080"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_tiamat(){
                $.getJSON('/ajax_tiamat/', function(ret){
                    $("#tiamat").empty();
                    $("#tiamat").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#tiamat').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_colossus(){
                $.getJSON('/ajax_colossus/', function(ret){
                    $("#colossus").empty();
                    $("#colossus").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#colossus').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_leviathan(){
                $.getJSON('/ajax_leviathan/', function(ret){
                    $("#leviathan").empty();
                    $("#leviathan").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#leviathan').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_yggdrasil(){
                $.getJSON('/ajax_yggdrasil/', function(ret){
                    $("#yggdrasil").empty();
                    $("#yggdrasil").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#yggdrasil').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_celeste(){
                $.getJSON('/ajax_celeste/', function(ret){
                    $("#celeste").empty();
                    $("#celeste").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#celeste').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            function ajax_luminiera(){
                $.getJSON('/ajax_luminiera/', function(ret){
                    $("#luminiera").empty();
                    $("#luminiera").append("<tr><th>Lvl</th><th>Code</th></tr>")
                    for (var i = 0; i <= ret.length - 1; i++) {
                        var level = ret[i].split(",")[1];
                        var code = ret[i].split(",")[2];
                        $('#luminiera').append("<tr><td>" + level +
                        '</td><td id="copy_to_clipboard"><div id="tip" style="position:absolute;visibility:hidden">Double click to copy to clipboard</div>' + code + "</td></tr>");
                    };
                    blue_and_copy();
                })}

            blue_and_copy();
            setInterval(ajax_tiamat, 40000);
            setInterval(ajax_colossus, 40000);
            setInterval(ajax_leviathan, 40000);
            setInterval(ajax_yggdrasil, 40000);
            setInterval(ajax_celeste, 20000);
            setInterval(ajax_luminiera, 20000);
            setInterval(ajax_all_boss, 10000);


        });
