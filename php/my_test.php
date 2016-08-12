<?php
header("content-type:text/html;charset=utf-8");
echo "你好， 世界！"."<br>";

#数组
    #索引数组
    $list1 = array(1, 2, 30, 12);
    echo "$list1[0], $list1[1], $list1[2]"."<br>";
        #获得数组长度
        echo count($list1)."<br>";

    #关联数组
    $list2 = array("xiaoming"=>"18", "xiaohong"=>"17");
    echo $list2["xiaoming"]."<br>";
    $list2["xiaofang"] = "19";
    echo '小芳年龄是'.$list2["xiaofang"]."<br>";

testListFor($list1);

#定义一个遍历数组的函数
function testListFor($list1){
    $list_count = count($list1);

    #for 语句的应用
    for($i = 0; $i < $list_count; $i++){
        echo $list1[$i].'<br>';
        testIf($list1[$i]);
    }
}

#定义一个试用if语句的函数
function testIf($x){
    if($x<10){
        echo $x."小于10".'<br>';
    }elseif($x>10 and $x < 20){
        echo $x."大于10小于20".'<br>';
    }else{
        echo $x."大天20".'<br>';
    }
}



?>