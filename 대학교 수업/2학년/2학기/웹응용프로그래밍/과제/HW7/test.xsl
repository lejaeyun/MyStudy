<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
	<html>
		<head>
			<title>HW7</title>
		</head>
		
		<script language="javascript"> 
			
			
			function start()
			{
				document.getElementById("appendButton").addEventListener("click", appendNode, false);
			}
			
			function appendNode()
			{
				var text="<student>";
				text +=  "<name>" + document.getElementById("Name") +"</name>";
				text +=  "<Student_id>"+ document.getElementById("Student_id") +"</Student_id>";
				text +=  "<Email>"+ document.getElementById("Email") +"</Email>";
				text +=  "<Address>"+ document.getElementById("Name") +"</Address>";
				text +=  "</student>";
				 
				if (window.DOMParser)
				{
					parser=new DOMParser();
					xmlDoc=parser.parseFromString(text,"text/xml");
				}
				else
				{
					xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
					xmlDoc.async=false;
					xmlDoc.loadXML(text); 
				} 
				 
				var addressNode = xmlDoc.createElement('img');
				var attNode = xmlDoc.createAttribute('src');
				attNode.nodeValue = document.getElementById("name")+".jpg";
				addressNode.setAttributeNode(attNode);
				xmlDoc.documentElement.appendChild(addressNode);
			}
			
			window.addEventListener("load", start, false);
		</script>
	
		<body>
			Name.<input type = "text" id = "Name"> <br>
			Student_id. <input type = "text" id = "Student_id"> <br>
			Email. <input type = "text" id = "Email"> <br>
			Address. <input type = "text" id = "Address"> <br>
			<xsl:element name="input">
				<xsl:attribute name="type">Submit</xsl:attribute>
				<xsl:attribute name = "value">Submit</xsl:attribute>
			</xsl:element>
			<input type = "button" id = "appendButton" value = "제출">
			
			<xsl:for-each select = "students">
				<xsl:value-of select="Name"/> <br/>
				<xsl:value-of select="Student_id"/> <br/>
				<xsl:value-of select="Address"/> <br/>
				<xsl:value-of select="Email"/> <br/>
				<img>
					<xsl:attribute name="SRC">
						<xsl:value-of select="Name/@picture"/>
					</xsl:attribute>
					<xsl:attribute name="align">
						<xsl:value-of select="left"/>
					</xsl:attribute>
				</img>
			</xsl:for-each>
		</body>	
	</html>
	</xsl:template>
</xsl:stylesheet>