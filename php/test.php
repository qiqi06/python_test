<?php
//定义命名空间
namespace MyProject;
header("content-type:text/html;charset=utf-8");

?>


<html>
<head>
	<title>Test of php</title>
	<style type="text/css">
		.centaier .contain{
			width: 480px;
			margin: 0 auto;
			font-family: "微软雅黑";
			font-size: 1.5em;
		}
	</style>
</head>
<body>
	<div class="centaier">
		<div class="contain">
			<?php
/*
Tip: php test
date; 20151203 10:00 
author:fan
*/
/*
$url=$_POST["mySelect"];
header("Location:$url");
exit();
*/

//定义常量
//区分大小写的常量名
define("GREETING", "欢迎访问 Runoob.com");
define("qiqi", "###################<br/>");

echo GREETING;    // 输出 "欢迎访问 Runoob.com"
echo '<br>';
// echo greeting;   // 输出 "greeting"

// 不区分大小写的常量名
define("GREETING2", "欢迎访问 Runoob.com", true);
echo greeting2;  // 输出 "欢迎访问 Runoob.com"

//开启错误提示
ini_set("display_errors", "On");
error_reporting(E_ALL | E_STRICT);

//类的定义， 注意没有()
class Basic {

//定义类的属性
//构造函数
	public $Name = "Basic";
	public function __construct($str){
		$this->Name=$str;
		echo "My name is ".$this->Name.'<br/>';
	}

	/*
	public function __destruct(){
		$this->Name=Null;
		echo "Name 这个对象已经被释放！";
	}
	*/

//定义方法（类里的函数叫方法）
//练习结构语句
	public function test_if(){
		echo "练习if语句".qiqi;
		$test1 = 80;
		if ($test1 > 60){
			echo "恭喜通过！<br/>";
		}else{
			echo "没用通过";
		}
		echo "练习swich语句".qiqi;
		$color = "red1";
		switch ($color) {
			case 'red':
			echo "The color is red <br/>";
			break;
			case 'green':
			echo 'The color is green <br/>';
			default:
			echo 'neither <br/>';
			break;
		}

//while循环
		echo "练习while语句".qiqi;
		$i=1;
		while($i<10){
			echo "The number is ".$i."<br/>";
			$i++;
		}		
		echo "for循环语句".qiqi;

//for循环语句
		for ($i=1;$i<10;$i++){
			echo $i."<br/>";
		}
	}

//魔术变量
	public function magic_test(){
		echo  "这是第".__LINE__." 行<br/>";
		echo "该文件位于".__FILE__."<br/>";
		echo "该文件位于".__DIR__."<br/>";
		echo "函数名为".__FUNCTION__."<br/>";
		echo "所用的类名为:".__CLASS__."<br/>";
		echo "所用的方法为:".__METHOD__."<br/>";
		echo "命名空间为:".__NAMESPACE__."<br/>";
	}
	//时间的调用
	public function datetime(){
		echo date("Y/m/d") . "<br>";
		echo date("Y.m.d") . "<br>";
		echo date("Y-m-d"). "<br/>";
	}

//类的static调用
	public static function Cubic($x){
		return $x * $x * $x;
	}

//实用创建ip方法
	public function IP($x, $y){
		for ($i=2;$i<$x+1;$i++){
			for ($j=2;$j<$y+1;$j++){
				echo "192.168.".$i.".".$j."<br/>";
			}
		}
	}
}

$test1 = new Basic("Apple");
echo "5的三次方为". Basic::Cubic(5)."<br/>";
$test1->IP(3, 6);
$test1->test_if();
$test1->magic_test();
$test1->datetime();
//$test2 = "3";
//isset($test2)，如果$test2设置了，为真。没设置为假。!isset($test2)为真
var_dump(!isset($test2));

?>
</div>
<div class="contain">
	<form method="post" action="redirect.php" >
		<select name="mySelect" size="1">
			<!-- 注意value 后面得加http://,否则重定向不了 -->
			<option value="http://www.baidu.com">百度</option>
			<option value="http://news.sina.com.cn">新浪新闻</option>
			<option value="http://www.hao123.com">Hao123</option>
		</select>
		<input type="submit" value="Go!">
	</form>
</div>
</div>
</body>
</html>