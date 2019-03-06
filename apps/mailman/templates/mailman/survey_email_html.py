from django.conf import settings


def write_html(email_text, link_html):
    return """
<html>
<body style="margin:0; padding: 0;">
<div align="center">
<table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="font-family: Arial,Helvetica,sans-serif; max-width: 700px;">
    <tbody><tr>
        <td align="center" style="padding-left:30px; padding-right:30px"><img width="200" alt="WorkElections" src="https://s3.amazonaws.com/voteworker/workelections_logo.png"></td>
        <td align="center" style="padding-left:30px; padding-right:30px"><img width="240" alt="Fair Elections Center" src="https://s3.amazonaws.com/voteworker/FEC_logo.gif"></td>
        <td>&nbsp;</td>
    </tr>
    <tr><td colspan="2" style="padding-top:50px; padding-bottom:20px"><hr></td></tr>
    <tr>
        <td colspan="2" align="left" valign="top" style="color:#555555; padding-left:30px; padding-right:30px; padding-bottom:20px;">
            <p>""" + email_text + """</p>
        </td>
    </tr>
    <tr><td colspan="4" align="center">""" + link_html + """</td></tr></tbody>
    <tr><td colspan="4" align="center" style="padding:10px; background-color:#BBBBBB; color:white; font-size:12px">
    1825 K St. NW  | Suite 450<br>
    Washington DC 20006<br>
    (202) 331-0114<br>
    <a style="color:#A5002F" href="mailto:info@fairelectionscenter.org">info@fairelectionscenter.org</a><br>
    </td></tr>
</table>
</div>
</body>
</html>
"""


def write_button(url, label):
    return '''
<td style="padding:10px"><div><!--[if mso]>
  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{url}" style="height:42px;v-text-anchor:middle;width:130px;" arcsize="10%" stroke="f" fillcolor="#3AAEE0">
    <w:anchorlock/>
    <center>
  <![endif]-->
      <a href="{url}"
style="background-color:#3AAEE0;border-radius:4px;color:#ffffff;display:inline-block;font-family:sans-serif;font-size:16px;font-weight:bold;line-height:42px;text-align:center;text-decoration:none;width:130px;-webkit-text-size-adjust:none;">{label}</a>
  <!--[if mso]>
    </center>
  </v:roundrect>
<![endif]--></div></td>'''.format(url=url, label=label)
