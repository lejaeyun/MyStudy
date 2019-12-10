<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
	<html>
		<head>
			<title>HW6</title>
		</head>
	<body>
			<xsl:for-each select = "students">
				<xsl:value-of select="name"/> <br/>
				<xsl:value-of select="student_id"/> <br/>
				<xsl:value-of select="address"/> <br/>
				<xsl:value-of select="email"/> <br/>
				<img>
					<xsl:attribute name="SRC">
						<xsl:value-of select="pic/@picture"/>
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