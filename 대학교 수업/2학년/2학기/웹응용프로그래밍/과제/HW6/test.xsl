<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
	<html>
		<head>
			<title>HW6</title>
		</head>
	<body>
			<xsl:for-each select = "students">
				<img>
					<xsl:attribute name="SRC">
						<xsl:value-of select="pic/@picture"/>
					</xsl:attribute>
					<xsl:attribute name="align">
						<xsl:value-of select="pic/@align"/>
					</xsl:attribute>
				</img>
				<h2><xsl:value-of select="name"/> </h2><br/>
				<xsl:value-of select="student_id"/><br/>
				<xsl:value-of select="address"/><br/>
				<xsl:value-of select="email"/><br/>
			</xsl:for-each>

	</body>	
	</html>
	</xsl:template>
</xsl:stylesheet>