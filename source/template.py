# encoding:utf-8
# python3.0

html_temp = '''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta name="generator" content="HTMLTestRunner 0.9.1"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>

    <link href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
    <script src="https://cdn.bootcss.com/echarts/3.8.5/echarts.common.min.js"></script>
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.3.1.js"></script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
    <!-- <script type="text/javascript" src="js/echarts.common.min.js"></script> -->
    <script type="text/javascript" class="init">
        $(document).ready(function() {
            $('#day1').DataTable();
            $('#day7').DataTable();
            $('#day30').DataTable();
        } );
    </script>
    <style type="text/css" media="screen">
        body        { font-family: Microsoft YaHei,Consolas,arial,sans-serif; font-size: 80%%; }
        table       { font-size: 100%%; }
        pre         { white-space: pre-wrap;word-wrap: break-word; }
        /* -- heading ---------------------------------------------------------------------- */
        h1 {
            font-size: 16pt;
            color: gray;
        }
        .heading {
            margin-top: 0ex;
            margin-bottom: 1ex;
        }
        .heading .attribute {
            margin-top: 1ex;
            margin-bottom: 0;
        }
        .heading .description {
            margin-top: 2ex;
            margin-bottom: 3ex;
        }
        /* -- css div popup ------------------------------------------------------------------------ */
        a.popup_link {
        }
        a.popup_link:hover {
            color: red;
        }
        .popup_window {
            display: none;
            position: relative;
            left: 0px;
            top: 0px;
            /*border: solid #627173 1px; */
            padding: 10px;
            /*background-color: #E6E6D6; */
            font-family: "Lucida Console", "Courier New", Courier, monospace;
            text-align: left;
            font-size: 8pt;
            /* width: 500px;*/
        }
        /* -- report ------------------------------------------------------------------------ */
        #show_detail_line {
            margin-top: 3ex;
            margin-bottom: 1ex;
        }
        #result_table {
            width: 99%%;
        }
        #header_row {
            font-weight: bold;
            color: #303641;
            background-color: #ebebeb;
        }
        #total_row  { font-weight: bold; }
        .passClass  { background-color: #bdedbc; }
        .failClass  { background-color: #ffefa4; }
        .errorClass { background-color: #ffc9c9; }
        .passCase   { color: #6c6; }
        .failCase   { color: #FF6600; font-weight: bold; }
        .errorCase  { color: #c00; font-weight: bold; }
        .hiddenRow  { display: none; }
        .testcase   { margin-left: 2em; }
        /* -- ending ---------------------------------------------------------------------- */
        #ending {
        }
        #div_base {
            position:absolute;
            top:0%%;
            left:5%%;
            right:5%%;
            width: auto;
            height: auto;
            margin: -15px 0 0 0;
        }
    </style>
</head>
<body>

<div id="div_base">

    <div class='page-header'>
        <h1>房屋价格情况统计</h1>
        <p class='attribute'><strong>统计时间:</strong> %s</p>
        <p class='attribute'><strong>运行时长:</strong> %s</p>
    </div>
%s
%s
%s
</div>
</body>
</html>
'''
