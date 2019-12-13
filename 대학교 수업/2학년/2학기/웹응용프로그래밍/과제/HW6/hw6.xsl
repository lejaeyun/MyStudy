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
					<xsl:attribute name="height">
						<xsl:value-of select="pic/@height"/>
					</xsl:attribute>
					<xsl:attribute name="width">
						<xsl:value-of select="pic/@width"/>
					</xsl:attribute>
					<xsl:attribute name="border">
						<xsl:value-of select="pic/@border"/>
					</xsl:attribute>
				</img>
				<h2> <xsl:value-of select="name"/> </h2> <br/><br/>
				학 번 : <xsl:value-of select="student_id"/><br/><br/>
				연락처 : <xsl:value-of select="address"/><br/><br/>
				학 교 :  <xsl:value-of select="school"/><br/><br/>
				이메일 : <xsl:value-of select="email"/><br/><br/>
			</xsl:for-each>

	</body>	
	</html>
	</xsl:template>
</xsl:stylesheet>