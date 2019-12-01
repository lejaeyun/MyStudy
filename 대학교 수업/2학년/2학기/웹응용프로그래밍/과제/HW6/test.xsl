<?xml version="1.0" encoding="euc-kr"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl">

	<xsl:template match="/">

		<img>
			<xsl:attribute name="SRC">
				<xsl:value-of select="students/student/pic/@picture"/>
			</xsl:attribute>
			<xsl:attribute align=left/>
		</img>

		<xsl:value-of select="students/student/name"/>
		<xsl:value-of select="students/student/student_id/"/>
		<xsl:value-of select="students/student/adress"/>
		<xsl:value-of select="students/student/email"/>

	</xsl:template>
</xsl:stylesheet>
