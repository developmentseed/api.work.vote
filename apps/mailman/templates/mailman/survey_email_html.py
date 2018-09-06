def write_html(link_html):
    return """
<html>
<body style="margin:0; padding: 0;">
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" align="center" width="100%"
        style="font-family: Arial,Helvetica,sans-serif; max-width: 700px;">
    <tr bgcolor="#000080">
        <td colspan="5" height="40">&nbsp;</td>
    </tr>
    <tr bgcolor="#000080">
        <td width="20">&nbsp;</td>
        <td width="20">&nbsp;</td>
        <td align="center" style="font-size: 29px; color:#FFF; font-weight: normal; letter-spacing: 1px; line-height: 1;
                        text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.2); font-family: Arial,Helvetica,sans-serif;">
            [SURVEY DRAFT] WorkElections.com Request for Information
        </td>
        <td width="20">&nbsp;</td>
        <td width="20">&nbsp;</td>
    </tr>
    <tr bgcolor="#000080">
        <td colspan="5" height="40">&nbsp;</td>
    </tr>
    <tr>
        <td height="10" colspan="5">&nbsp;</td>
    </tr>
    <tr>
        <td>&nbsp;</td>
        <td colspan="3" align="left" valign="top" style="color:#666666; font-size: 13px;">
            
                <p>Thank you for your participation in our survey for WorkElections.com. <br> Please click on the link corresponding with the jurisdiction for which you would like to update information.</p>
            
        </td>
        <td>&nbsp;</td>
    </tr>

    
        <tr>
            <td colspan="5" height="30">&nbsp;</td>
        </tr>
        <tr>
            <td>&nbsp;</td>
            <td colspan="3">
                <table border="0" cellpadding="0" cellspacing="0" align="left"
                    <tr>
                        <td align="center" valign="center">""" + link_html + """
                        </td>
                    </tr>
                </table>
            </td>
            <td>&nbsp;</td>
        </tr>
        <tr>
            <td colspan="5" height="30">&nbsp;</td>
        </tr>
    <tr>
        <td height="20" colspan="5">&nbsp;</td>
    </tr>
    <tr>
        <td height="20" colspan="5">&nbsp;</td>
    </tr>
</table>
</div>
</body>
</html>
"""