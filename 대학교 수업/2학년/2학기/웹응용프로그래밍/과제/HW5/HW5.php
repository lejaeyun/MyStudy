<?php
header('Content-Type: text/html; charset=UTF-8');
?>
<!DOCTYPE html>
<html>

	<head>
		<title>HW5</title>
		<style>
			h1,h3 { text-align : left; font-family: tahoma, geneva, sans-serif;}
			p {marin-left: 5%; margin-right: 5%; font-family: arial, helvetica, sans-serif;}
			ul {margin-left: 10%;}
			a {text-decoration: none;}
			a:hover {text-decoration: none;}
			.nav { width: 100%; border-top: 3px dashed blue; padding-top: 10px;}
			.hilighted {background-color: yellow;}
			input {width: 150px;}
			form > p {margin: 0px;}
		</style>
	</head>
	<?php
	
	$id;
	
	function start()
	{
		$servername = "164.125.36.45";
		$username = "201624548";
		$password = "201624548";

		$conn = new mysqli($servername, $username, $password);
		
		$sql = "CREATE DATABASE test";
		mysqli_query($conn,$sql);
		
		$sql = "USE test";
		mysqli_query($conn,$sql);
		
		$sql = "drop table problem";
		mysqli_query($conn,$sql);
		
		$sql = "CREATE TABLE problem(
				id INT(6)NOT NULL,
				title VARCHAR(1000) NOT NULL,
				exp VARCHAR(1000) NOT NULL,
				ans1 VARCHAR(1000) NOT NULL,
				ans2 VARCHAR(1000) NOT NULL,
				ans3 VARCHAR(1000) NOT NULL,
				ans4 VARCHAR(1000) NOT NULL,
				ans5 VARCHAR(1000) NOT NULL,
				ans VARCHAR(2) NOT NULL,
				CONSTRAINT PK_MY_TABLE PRIMARY KEY(id) )";
		mysqli_query($conn,$sql);
		
		$sql = "INSERT INTO problem	VALUES( $id, '$title', '$exp', '$ans1', '$ans2', '$ans3', '$ans4', '$ans5', '$ans')";
		mysqli_query($conn,$sql);
		
		mysqli_close($conn);
	}
	
	?>
	
	<script language="javascript"> 
	
		var currentNode;
		var idcount;
		var nowindex;
		var item;
		var ans;
		
		function start()
		{
			idcount = 1;
			alert("start");
			<?php start();?>
			document.getElementById("appendButton").addEventListener("click", appendNode, false);
			document.getElementById("replaceButton").addEventListener("click", replace, false);
			document.getElementById("solveButton").addEventListener("click", solve, false);
			document.getElementById("openbtn").addEventListener("click", openBtn, false);
			currentNode = document.getElementById("para");
		}
		
		function openBtn() {
			var con = document.getElementById("replaceproblem");
			con.style.display = 'none';
			var con = document.getElementById("solveproblem");
			con.style.display = 'none';
			var con = document.getElementById("postproblem");
			con.style.display = 'block';
		}
		
		function selectedBtn() {
			if (this.id.match("solve"))
				solvedisplay(this.id);
			else if (this.id.match("replace"))
				replacedisplay(this.id);
			else if (this.id.match("remove"))
				remove(this.id);
		}
		
		var name;
		function setItem(tmpitem) {
			item = tmpitem;
		}
		
		function Setitem(id, item) {
			httpRequest = new XMLHttpRequest();
			var tmp = item.split(',');
			var str = 'id='+id;
			var str = str + '&title='+tmp[0];
			var str = str + '&ans='+tmp[6];
			var str = str + '&exp='+tmp[7];
			var str = str + '&ans1='+tmp[1];
			var str = str + '&ans2='+tmp[2];
			var str = str + '&ans3='+tmp[3];
			var str = str + '&ans4='+tmp[4];
			var str = str + '&ans5='+tmp[5];
			httpRequest.open('GET', 'test.php?'+str);
			httpRequest.send();
			httpRequest.close();
		}

		function ReturnItem(id,type) {
			
			httpRequest = new XMLHttpRequest();
			var str = 'id='+id;
			httpRequest.open('GET', 'test2.php?'+str);
			httpRequest.send();
			httpRequest.onreadystatechange = function () { 
				if (httpRequest.readyState == 4 && httpRequest.status == 200) {
					var result = JSON.parse(httpRequest.responseText);
					if (type == 1) {
						var answer = result.split(',');
						ans = answer[6];
						document.getElementById("solve").value = answer[0];
						document.getElementById("solve1").value = answer[1];
						document.getElementById("solve2").value = answer[2];
						document.getElementById("solve3").value = answer[3];
						document.getElementById("solve4").value = answer[4];
						document.getElementById("solve5").value = answer[5];
						document.getElementById("solve6").value = "";
						document.getElementById("solve7").value = answer[7];
						httpRequest.close();
					}
					else if (type == 2){
						var answer = result.split(',');
						document.getElementById("replace").value = answer[0];
						document.getElementById("replace1").value = answer[1];
						document.getElementById("replace2").value = answer[2];
						document.getElementById("replace3").value = answer[3];
						document.getElementById("replace4").value = answer[4];
						document.getElementById("replace5").value = answer[5];
						document.getElementById("replace6").value = answer[6];
						document.getElementById("replace7").value = answer[7];
						httpRequest.close();
					}
				}
			}
			alert(result);
		}

		
		function appendNode()
		{
		
			var newNode = createNewNode( document.getElementById("append").value , 1 );
			currentNode.append(newNode);
			
			var item = document.getElementById("append").value + ',' + document.getElementById("append1").value + ',' + document.getElementById("append2").value + ',' + document.getElementById("append3").value + ',' + document.getElementById("append4").value + ',' + document.getElementById("append5").value + ',' + document.getElementById("append6").value + ',' + document.getElementById("append7").value;

			document.getElementById("append").value = "";
			document.getElementById("append1").value = "";
			document.getElementById("append2").value = "";
			document.getElementById("append3").value = "";
			document.getElementById("append4").value = "";
			document.getElementById("append5").value = "";
			document.getElementById("append6").value = "";
			document.getElementById("append7").value = "";
			
			var con = document.getElementById("postproblem");
			con.style.display = 'none';
			
			Setitem(idcount-1, item);
			
		}
		
		function setbutton(nownode)
		{
			
			var jbBtn = document.createElement( 'button' );
			var jbBtnText = document.createTextNode( '풀기' );
			jbBtn.appendChild( jbBtnText );
			jbBtn.setAttribute("id", "solve," + (idcount-1));
			jbBtn.addEventListener("click", selectedBtn, false);
			nownode.appendChild( jbBtn );
			
			var jbBtn = document.createElement( 'button' );
			var jbBtnText = document.createTextNode( '수정' );
			jbBtn.appendChild( jbBtnText );
			jbBtn.setAttribute("id", "replace," + (idcount-1));
			jbBtn.addEventListener("click", selectedBtn, false);
			nownode.appendChild( jbBtn );
			
			var jbBtn = document.createElement( 'button' );
			var jbBtnText = document.createTextNode( '제거' );
			jbBtn.appendChild( jbBtnText );
			jbBtn.setAttribute("id", "remove," + (idcount-1));
			jbBtn.addEventListener("click", selectedBtn, false);
			nownode.appendChild( jbBtn );
		}
		
		function solvedisplay(id)
		{
			var con = document.getElementById("replaceproblem");
			con.style.display = 'none';
			var con = document.getElementById("solveproblem");
			con.style.display = 'block';
			var con = document.getElementById("postproblem");
			con.style.display = 'none';
			
			nowindex = id.split(',')[1];
			ReturnItem(nowindex, 1)
		}
		
		
		function replacedisplay(id)
		{
			var con = document.getElementById("replaceproblem");
			con.style.display = 'block';
			var con = document.getElementById("solveproblem");
			con.style.display = 'none';
			var con = document.getElementById("postproblem");
			con.style.display = 'none';
			
			nowindex = id.split(',')[1];
			ReturnItem(nowindex, 2)
		}
		
		function replace()
		{
			var item = document.getElementById("replace").value + ',' + document.getElementById("replace1").value + ',' + document.getElementById("replace2").value + ',' + document.getElementById("replace3").value + ',' + document.getElementById("replace4").value + ',' + document.getElementById("replace5").value + ',' + document.getElementById("replace6").value + ',' + document.getElementById("replace7").value;

			alert("문제 "+nowindex+"번 수정되었습니다");
			
			document.getElementById("label" + nowindex).innerHTML = "[문제" + nowindex + "]" + document.getElementById("replace").value;
			
			var con = document.getElementById("replaceproblem");
			con.style.display = 'none';
			
			Setitem(nowindex, item);
			
		}
		
		function solve()
		{
			
			if (document.getElementById("solve6").value == ans)
				alert('맞았습니다');
			else
				alert('틀렸습니다')
				
			var con = document.getElementById("solveproblem");
			con.style.display = 'none';
		}
		
		function remove(target)
		{
			var con = document.getElementById("replaceproblem");
			con.style.display = 'none';
			var con = document.getElementById("solveproblem");
			con.style.display = 'none';
			var con = document.getElementById("postproblem");
			con.style.display = 'none';
			
			if (currentNode.parentNode == document.body )
				alert("Can't remove a top-level element.");
			else
			{
				var targetid = '문제' + target.split(',')[1]
				var oldNode = document.getElementById(targetid);
				alert(targetid+"번 제거되었습니다");
				oldNode.remove();
			}
		}
		
		
		function createNewNode(text,type)
		{
			var newNode = document.createElement("li");
			nodeId = "문제" + idcount;
			newNode.setAttribute("id", nodeId);
			text = "[" + nodeId + "]" + text;
			var labelNode = document.createElement("label");
			labelNode.setAttribute("id", "label" + idcount);
			idcount++;
			labelNode.innerHTML = text;
			newNode.appendChild( labelNode );
			setbutton(newNode, idcount - 1)
			return newNode;
		}
		
		window.addEventListener("load", start, false);
		
	</script>
	
	<body oncontextmenu="return false" ondragstart="return false" onselectstart="return false">
	
		<h1 id = "bigheading" class = "highlighted">
			Problem 3 문제 은행
		<h1>
		<p id = "para">문제 내역
				<input type = "button" id = "openbtn" value = "문제 제출하기">
		</p>
		
		<div id = "nav" class = "nav">
			<form onsubmit = "return false" action = "#">
				
				<div id = "postproblem" style = "display : none">
					<p>	문제 Title<input type = "text" id = "append"> <br>
						설명. <input type = "text" id = "append7"> <br>
						Select 1. <input type = "text" id = "append1"> <br>
						Select 2. <input type = "text" id = "append2"> <br>
						Select 3. <input type = "text" id = "append3"> <br>
						Select 4. <input type = "text" id = "append4"> <br>
						Select 5. <input type = "text" id = "append5"> <br>
						정답 <input type = "text" id = "append6">
						<input type = "button" id = "appendButton" value = "문제 제출">
					</p>
				</div>
				
				<div id = "replaceproblem" style = "display : none">
					<p>	문제 Title<input type = "text" id = "replace"> <br>
						설명. <input type = "text" id = "replace7"> <br>
						Select 1. <input type = "text" id = "replace1"> <br>
						Select 2. <input type = "text" id = "replace2"> <br>
						Select 3. <input type = "text" id = "replace3"> <br>
						Select 4. <input type = "text" id = "replace4"> <br>
						Select 5. <input type = "text" id = "replace5"> <br>
						정답 <input type = "text" id = "replace6">
						<input type = "button" id = "replaceButton" value = "문제 수정">
					</p>
				</div>
				
				<div id = "solveproblem" style = "display : none">
					<p>	문제 Title<input type = "text" id = "solve"> <br>
						설명. <input type = "text" id = "solve7"> <br>
						Select 1. <input type = "text" id = "solve1"> <br>
						Select 2. <input type = "text" id = "solve2"> <br>
						Select 3. <input type = "text" id = "solve3"> <br>
						Select 4. <input type = "text" id = "solve4"> <br>
						Select 5. <input type = "text" id = "solve5"> <br>
						정답 <input type = "text" id = "solve6">
						<input type = "button" id = "solveButton" value = "정답 제출">
					</p>
				</div>
			</form>
			<form>
				<input type="hidden" name="name" id="name" value="<?php $result?>">
			</form>
		</div>
	</body>
</html>
