/*
获得用户详细信息，在个人主页使用
load_user_detail：获得用户详细信息
*/

function load_user_detail(uid=null)
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function()
    {
        var str = xmlhttp.responseText;
        var json_str = JSON.parse(str);
        if (json_str["status"] == 0)
        {
            document.getElementById("main").innerHTML = "<h1>该用户不存在！</h1>"
            return
        }
        document.title = json_str["data"]["username"]+"的主页 - 古典社会模拟 CIVITAS2";
        document.getElementById("avatar").innerHTML = "<p class=\" main-subchar\"><img src=\"https://api.trickydeath.xyz/getavatar/?uid="
            +get_parameter_value("uid")+"\"  class=\"img-thumbnail\" width=\"100px\" height=\"100px\"/>"
            +json_str["data"]["username"]+"</p>";
    }
    if (uid == null)
    {
        xmlhttp.open("GET","https://api.trickydeath.xyz/getuserdetail/",true);
    }
    else
    {
        xmlhttp.open("GET","https://api.trickydeath.xyz/getuserdetail/?uid=" + uid,true);
    }
    xmlhttp.withCredentials = true;
    xmlhttp.send();
}