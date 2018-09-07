from django.conf import settings
import os
def write_html(email_text, link_html):
    return """
<html>
<body style="margin:0; padding: 0;">
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="font-family: Arial,Helvetica,sans-serif; max-width: 700px;">
       <tbody><tr bgcolor="#39446f">
           <td colspan="5" height="40">&nbsp;</td>
       </tr>
           <tr bgcolor="#39446f"></tr>
       <tr bgcolor="#39446f">
           <td width="20">&nbsp;</td>
           <td width="20">&nbsp;</td>
           <td align="center" style="font-size: 29px; color:#FFF; font-weight: normal; letter-spacing: 1px; line-height: 1;
                           text-shadow: -1px -1px 1px rgba(0, 0, 0, 0.2); font-family: Arial,Helvetica,sans-serif;">
    <img alt="WorkElections" src="https://s3.amazonaws.com/voteworker/workelections.png">
<br><br>
              [SURVEY DRAFT] WorkElections.com Request for Information
           </td>
           <td width="20">&nbsp;</td>
           <td width="20">&nbsp;</td>
       </tr>
       <tr bgcolor="#39446f">
           <td colspan="5" height="40">&nbsp;</td>
       </tr>   
       <tr>
           <td height="20" colspan="5">&nbsp;</td>
       </tr>
    <tr>
        <td>&nbsp;</td>
        <td colspan="3" align="left" valign="top" style="color:#666666; font-size: 13px;">
            
                <p>""" + email_text + """</p>
            
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