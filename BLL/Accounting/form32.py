import os
from datetime import datetime

def generate_account_request(name, mis2, year2, data1, data3, data6):
    current_date = datetime.now().date()
    year = current_date.year
    mis = current_date.month
    data1 = float(data1)
    data3 = float(data3)
    data6 = float(data6)
    data2 = data1 * 0.02
    data4 = float(data2)+float(data3)
    data5 = data4
    if data6 > data5:
        data7 = data6-data5
        data8 = "-"
    elif data6 < data5:
        data8 = data5 - data6
        data7 = "-"
    else:
        data8 = "-"
        data7 = "-"

    date2 = current_date.strftime("%d-%m-%Y")

    html_content = f"""
<html xmlns:v="urn:schemas-microsoft-com:vml"
xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:w="urn:schemas-microsoft-com:office:word"
xmlns:m="http://schemas.microsoft.com/office/2004/12/omml"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta charset="utf-8">
<meta http-equiv=Content-Type content="text/html; charset=windows-1251">
<meta name=ProgId content=Word.Document>
<meta name=Generator content="Microsoft Word 15">
<meta name=Originator content="Microsoft Word 15">

</head>

<body lang=UK style='tab-interval:35.4pt'>
<div class=WordSection1>
<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="33%" style='width:33.08%;border:solid windowtext 1.0pt;background:
  white;padding:3.4pt 2.85pt 3.4pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Відмітка про одержання<br>
  (штамп контролюючого органу)<o:p></o:p></span></p>
  </td>
  <td width="66%" valign=top style='width:66.92%;background:white;padding:3.4pt 0cm 3.4pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-top:19.85pt;margin-right:0cm;margin-bottom:
  0cm;margin-left:462.9pt;margin-bottom:.0001pt;mso-line-height-alt:9.1pt'><span
  style='color:black;mso-fareast-language:UK'>ЗАТВЕРДЖЕНО<br>
  Наказ Міністерства фінансів України<br>
  26 квітня 2022 року № 124<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="5%" rowspan=3 style='width:5.02%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>1<o:p></o:p></span></p>
  </td>
  <td width="62%" rowspan=3 style='width:62.42%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><b><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>ПОДАТКОВА ДЕКЛАРАЦІЯ ПЛАТНИКА ЄДИНОГО
  ПОДАТКУ ТРЕТЬОЇ ГРУПИ<br>
  НА ПЕРІОД ДІЇ ВОЄННОГО, НАДЗВИЧАЙНОГО СТАНУ В УКРАЇНІ</span></b><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
  <td width="5%" valign=top style='width:5.74%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>01<o:p></o:p></span></p>
  </td>
  <td width="10%" valign=top style='width:10.04%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black;mso-color-alt:
  windowtext;mso-fareast-language:UK'>Х<o:p></o:p></span></p>
  </td>
  <td width="16%" valign=top style='width:16.78%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Звітна<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="5%" valign=top style='width:5.74%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>02<o:p></o:p></span></p>
  </td>
  <td width="10%" valign=top style='width:10.04%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="16%" valign=top style='width:16.78%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Звітна нова<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="5%" valign=top style='width:5.74%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>03<o:p></o:p></span></p>
  </td>
  <td width="10%" valign=top style='width:10.04%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="16%" valign=top style='width:16.78%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Уточнююча<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="5%" style='width:5.16%;border:solid black 1.0pt;background:white;
  padding:2.85pt 3.4pt 2.85pt 3.4pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>2<o:p></o:p></span></p>
  </td>
  <td width="94%" valign=top style='width:94.84%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Податковий (звітний) період:<o:p></o:p></span></p>
  <p class=MsoNormal style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;
  margin-left:39.7pt;margin-bottom:.0001pt;mso-line-height-alt:8.95pt'><span
  lang=EN-US style='color:black;letter-spacing:-.1pt;mso-ansi-language:EN-US;
  mso-fareast-language:UK'>{mis}</span><span lang=EN-US style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'> </span><span style='color:
  black;letter-spacing:-.1pt;mso-fareast-language:UK'>місяць </span><span
  lang=EN-US style='color:black;letter-spacing:-.1pt;mso-ansi-language:EN-US;
  mso-fareast-language:UK'>{year}</span><span style='color:black;letter-spacing:
  -.1pt;mso-fareast-language:UK'> року<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="5%" style='width:5.16%;border:solid black 1.0pt;background:white;
  padding:2.85pt 3.4pt 2.85pt 3.4pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>3<o:p></o:p></span></p>
  </td>
  <td width="94%" valign=top style='width:94.84%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Податковий (звітний) період, який <span class=SpellE>уточнюється</span><o:p></o:p></span></p>
  <p class=MsoNormal style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;
  margin-left:39.7pt;margin-bottom:.0001pt;mso-line-height-alt:8.95pt'><span
  lang=EN-US style='color:black;letter-spacing:-.1pt;mso-ansi-language:EN-US;
  mso-fareast-language:UK'>{mis2}</span><span lang=EN-US style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'> </span><span style='color:
  black;letter-spacing:-.1pt;mso-fareast-language:UK'>місяць </span><span
  lang=EN-US style='color:black;letter-spacing:-.1pt;mso-ansi-language:EN-US;
  mso-fareast-language:UK'>{year2}</span><span style='color:black;letter-spacing:
  -.1pt;mso-fareast-language:UK'> року<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="5%" style='width:5.16%;border:solid black 1.0pt;background:white;
  padding:2.85pt 3.4pt 2.85pt 3.4pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>4<o:p></o:p></span></p>
  </td>
  <td width="94%" valign=top style='width:94.84%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal align=center style='margin-top:.85pt;margin-right:0cm;
margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
mso-line-height-alt:7.5pt;background:white'><span style='font-size:10.0pt;
color:black;mso-fareast-language:UK'>(найменування контролюючого органу, до якого
подається звітність)<o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="40%" valign=top style='width:40.38%;border:none;border-right:solid windowtext 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Фізична особа — підприємець<o:p></o:p></span></p>
  </td>
  <td width="4%" valign=top style='width:4.82%;border:solid windowtext 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="50%" valign=top style='width:50.0%;border:none;border-right:solid windowtext 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;
  margin-left:70.85pt;margin-bottom:.0001pt;mso-line-height-alt:8.95pt'><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'>Юридична особа<o:p></o:p></span></p>
  </td>
  <td width="4%" valign=top style='width:4.8%;border:solid windowtext 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black;mso-fareast-language:
  UK'>Х<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="5%" rowspan=2 style='width:5.16%;border:solid black 1.0pt;
  background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>5<o:p></o:p></span></p>
  </td>
  <td width="19%" rowspan=2 style='width:19.88%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Платник<o:p></o:p></span></p>
  </td>
  <td width="74%" valign=top style='width:74.96%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><span class=SpellE>Company</span> <span
  class=SpellE>Knot</span> <span class=SpellE>Group</span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="74%" valign=top style='width:74.96%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 3.4pt 2.85pt 3.4pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal align=center style='margin-top:.85pt;margin-right:0cm;
margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
mso-line-height-alt:7.5pt;background:white'><span style='font-size:10.0pt;
color:black;mso-fareast-language:UK'>(Найменування суб’єкта господарювання для юридичної
особи або прізвище, ім’я та по батькові (за наявності) для фізичної особи - підприємця)<o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="5%" rowspan=2 style='width:5.14%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>6<o:p></o:p></span></p>
  </td>
  <td width="65%" rowspan=2 style='width:65.44%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Код за ЄДРПОУ, реєстраційний номер облікової картки платника податків або
  серія (за наявності) та номер паспорта<sup>1</sup><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span>1<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>2<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>3<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>4<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>5<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>6<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>7<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>8<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>9<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border:none;border-bottom:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="5%" rowspan=4 style='width:5.14%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>7<o:p></o:p></span></p>
  </td>
  <td width="19%" rowspan=3 style='width:19.82%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Податкова адреса<o:p></o:p></span></p>
  </td>
  <td width="75%" colspan=12 valign=top style='width:75.04%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span>М. Львів, вул. В’язова 34А<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="75%" colspan=12 valign=top style='width:75.04%;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:3.0pt'>
  <td width="75%" colspan=12 valign=top style='width:75.04%;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-top:.85pt;margin-right:0cm;
  margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
  mso-line-height-alt:7.5pt'><span style='font-size:10.0pt;color:black;
  mso-fareast-language:UK'>(податкова адреса (місце проживання) платника
  податку)<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="19%" valign=top style='width:19.82%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Електронна адреса<o:p></o:p></span></p>
  </td>
  <td width="32%" valign=top style='width:32.96%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><span
  style='mso-spacerun:yes'> </span>test@test.com<o:p></o:p></span></p>
  </td>
  <td width="12%" valign=top style='width:12.74%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>Телефон<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.92%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span>0<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>1<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>2<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>3<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.92%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>4<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>5<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>6<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>7<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.92%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>8<o:p></o:p></span></p>
  </td>
  <td width="2%" valign=top style='width:2.94%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'>9<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<p class=MsoNormal align=center style='margin-top:2.85pt;margin-right:0cm;
margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'>І. Розрахунок податкових зобов’язань
з єдиного податку<o:p></o:p></span></b></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="73%" style='width:73.82%;border:solid black 1.0pt;background:white;
  padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Показники<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border:solid black 1.0pt;border-left:none;
  background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Код рядка<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border:solid black 1.0pt;border-left:
  none;background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Сума,<br>
  грн, коп.<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Обсяг доходу за податковий (звітний) місяць, що оподатковується за ставкою
  2 відсотки доходу<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>01<o:p></o:p></span></p>
  </td>
  <td width="17%" valign=top style='width:17.38%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data1}<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Сума податкових зобов’язань за податковий (звітний) місяць (рядок 01 x 2 відсотки)<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>02<o:p></o:p></span></p>
  </td>
  <td width="17%" valign=top style='width:17.38%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data2}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<p class=MsoNormal align=center style='margin-top:2.85pt;margin-right:0cm;
margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'>ІІ. Розрахунок податкових зобов’язань
з єдиного податку з урахуванням позитивного значення різниці між сумою загального
мінімального податкового зобов’язання та загальною сумою сплачених податків, зборів,
платежів та витрат на оренду земельних ділянок<sup>2</sup><o:p></o:p></span></b></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="73%" style='width:73.82%;border:solid black 1.0pt;background:white;
  padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Показники<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border:solid black 1.0pt;border-left:none;
  background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Код рядка<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border:solid black 1.0pt;border-left:
  none;background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Сума,<br>
  грн, коп.<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Позитивне значення різниці між сумою загального мінімального<br>
  податкового зобов’язання та загальною сумою сплачених податків, зборів, платежів
  та витрат на оренду земельних ділянок (рядок 04 колонки 3 розділу ІІ додатка 1)<sup>2</sup><o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>03<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data3}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Сума єдиного податку до сплати з <span class=SpellE>урахуваням</span> позитивного
  значення різниці між сумою загального мінімального податкового зобов’язання та
  загальною сумою сплачених податків, зборів, платежів та витрат на оренду земельних
  ділянок (рядок 02 + рядок 03)<sup>3</sup><o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>04<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data4}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<p class=MsoNormal align=center style='margin-top:2.85pt;margin-right:0cm;
margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'>ІІІ. Визначення податкових зобов’язань
у зв’язку з виправленням самостійно виявлених помилок<o:p></o:p></span></b></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="73%" style='width:73.82%;border:solid black 1.0pt;background:white;
  padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Показники<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border:solid black 1.0pt;border-left:none;
  background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Код рядка<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border:solid black 1.0pt;border-left:
  none;background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Сума,<br>
  грн, коп.<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Сума єдиного податку за даними раніше поданої декларації, що <span
  class=SpellE>уточнюється</span><br>
  (рядок 02 або 04 декларації, що <span class=SpellE>уточнюється</span>)<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>05<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data5}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Уточнена сума податкових зобов’язань за податковий (звітний) період,<br>
  у якому виявлена помилка<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>06<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data6}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Сума єдиного податку до збільшення у зв’язку з виправленням помилки<br>
  (рядок 06 – рядок 05, якщо рядок 06 &gt; рядка 05)<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>07<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data7}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="73%" valign=top style='width:73.82%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Сума єдиного податку до зменшення у зв’язку з виправленням помилки<br>
  (рядок 05 – рядок 06, якщо рядок 05 &gt; рядка 06)<o:p></o:p></span></p>
  </td>
  <td width="8%" style='width:8.82%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>08<o:p></o:p></span></p>
  </td>
  <td width="17%" style='width:17.38%;border-top:none;border-left:none;
  border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;background:
  white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span lang=EN-US style='color:black;
  mso-color-alt:windowtext;mso-ansi-language:EN-US;mso-fareast-language:UK'>{data8}</span><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0
 style='margin-left:2.85pt;border-collapse:collapse;mso-yfti-tbllook:160;
 mso-padding-alt:0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width=435 colspan=2 valign=top style='width:326.0pt;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Доповнення до податкової декларації (заповнюється і додається відповідно до
  пункту 46.4<br>
  статті 46 глави 2 розділу ІІ Податкового кодексу України)<span
  style='mso-spacerun:yes'>                                                              
  </span>на:<o:p></o:p></span></p>
  </td>
  <td width=45 valign=top style='width:34.0pt;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width=34 valign=bottom style='width:25.5pt;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span class=SpellE><span style='color:black;letter-spacing:-.1pt;
  mso-fareast-language:UK'>арк</span></span><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>.<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width=30 style='width:22.5pt;border:solid black 1.0pt;border-top:none;
  background:white;padding:2.85pt 0cm 3.55pt 0cm;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>№ з/п<o:p></o:p></span></p>
  </td>
  <td width=484 colspan=3 style='width:363.0pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 3.55pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.05pt'><span style='color:black;
  mso-fareast-language:UK'>Зміст доповнення<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:3.0pt'>
  <td width=30 valign=top style='width:22.5pt;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width=484 colspan=3 valign=top style='width:363.0pt;border-top:none;
  border-left:none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;mso-yfti-lastrow:yes'>
  <td width=44 style='width:33.0pt;background:white;padding:0cm 0cm 0cm 0cm'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-fareast-language:UK'><span
  style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width=581 style='width:435.75pt;background:white;padding:0cm 0cm 0cm 0cm'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-fareast-language:UK'><span
  style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width=65 style='width:48.75pt;background:white;padding:0cm 0cm 0cm 0cm'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-fareast-language:UK'><span
  style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
  <td width=50 style='width:37.5pt;background:white;padding:0cm 0cm 0cm 0cm'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-fareast-language:UK'><span
  style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span><o:p></o:p></span></p>

<p class=MsoNormal style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;
margin-left:2.85pt;margin-bottom:.0001pt;mso-line-height-alt:8.95pt;background:
white'><b><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
UK'>До декларації додається:</span></b><span style='color:black;letter-spacing:
-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="5%" valign=top style='width:5.14%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>1<o:p></o:p></span></p>
  </td>
  <td width="88%" valign=top style='width:88.24%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.15pt;mso-fareast-language:
  UK'>Додаток 1 «Розрахунок загального мінімального податкового зобов’язання за
  податковий (звітний) рік»<sup>2</sup></span><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
  <td width="6%" valign=top style='width:6.62%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black;mso-fareast-language:
  UK'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="5%" valign=top style='width:5.14%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>2<o:p></o:p></span></p>
  </td>
  <td width="88%" valign=top style='width:88.24%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.3pt;mso-fareast-language:
  UK'>Додаток 2 «Відомості про суми нарахованого доходу застрахованих осіб та суми
  нарахованого єдиного внеску»<sup>4</sup></span><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
  <td width="6%" valign=top style='width:6.62%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;line-height:normal'><span style='color:black;mso-fareast-language:
  UK'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span></span></b><span style='color:black;
mso-fareast-language:UK'><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes;
  height:3.0pt'>
  <td width="93%" valign=top style='width:93.38%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.15pt;mso-fareast-language:
  UK'>Додаток 2 «Відомості про суми нарахованого доходу застрахованих осіб та суми
  нарахованого єдиного внеску»</span><span style='color:black;letter-spacing:
  -.1pt;mso-fareast-language:UK'> подається поза межами звітного (податкового) періоду
  для призначення пенсії/матеріального забезпечення, страхових виплат»<sup>5</sup><o:p></o:p></span></p>
  </td>
  <td width="6%" valign=top style='width:6.62%;border:solid black 1.0pt;
  border-left:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span></span></b><span style='color:black;
mso-fareast-language:UK'><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="100%" colspan=2 valign=top style='width:100.0%;border:solid black 1.0pt;
  background:white;padding:4.25pt 2.85pt 4.25pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Дата подання декларації:<span style='mso-spacerun:yes'>          </span></span><span
  lang=EN-US style='color:black;mso-color-alt:windowtext;mso-ansi-language:
  EN-US;mso-fareast-language:UK;mso-no-proof:yes'>{date2}</span><span
  lang=EN-US style='color:black;letter-spacing:-.1pt;mso-ansi-language:EN-US;
  mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="100%" colspan=2 valign=top style='width:100.0%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><b><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>Інформація про особу, уповноважену
  на заповнення декларації</span></b><span style='color:black;letter-spacing:
  -.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:3.0pt'>
  <td width="59%" valign=top style='width:59.54%;border:none;border-left:solid black 1.0pt;
  background:white;padding:5.65pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Прізвище, ім’я, по батькові (за наявності) керівника<br>
  (уповноваженої особи) / фізичної особи (законного представника)<o:p></o:p></span></p>
  </td>
  <td width="40%" valign=top style='width:40.46%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:5.65pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'><span style='color:black;mso-color-alt:windowtext;mso-fareast-language:
  UK'><span style='mso-spacerun:yes'> </span><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:3.0pt'>
  <td width="59%" valign=top style='width:59.54%;border:none;border-left:solid black 1.0pt;
  background:white;padding:5.65pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Реєстраційний номер облікової картки платника податків<br>
  або серія (за наявності) та номер паспорта<sup>1</sup><o:p></o:p></span></p>
  </td>
  <td width="40%" valign=top style='width:40.46%;border:none;border-right:solid black 1.0pt;
  background:white;padding:5.65pt 0cm 2.85pt 2.85pt;height:3.0pt'>
  <div align=right>
  <table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
   style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
   mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
   <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
    <td valign=top style='border:solid windowtext 1.0pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>1<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>2<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>3<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>4<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>5<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>6<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>7<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>8<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>9<o:p></o:p></span></p>
    </td>
   </tr>
  </table>
  </div>
  <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;height:3.0pt'>
  <td width="59%" valign=top style='width:59.54%;border:none;border-left:solid black 1.0pt;
  background:white;padding:5.65pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Прізвище, ім’я, по батькові (за наявності) головного бухгалтера (особи, відповідальної
  за ведення бухгалтерського обліку)<o:p></o:p></span></p>
  </td>
  <td width="40%" valign=top style='width:40.46%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:5.65pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;line-height:normal'><span style='color:black;mso-color-alt:
  windowtext;mso-fareast-language:UK'><span style='mso-spacerun:yes'> </span></span><span
  lang=EN-US style='color:black;mso-color-alt:windowtext;mso-ansi-language:
  EN-US;mso-fareast-language:UK'>{name}<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="59%" valign=top style='width:59.54%;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid black 1.0pt;border-right:none;
  background:white;padding:5.65pt 2.85pt 5.65pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;mso-line-height-alt:
  8.95pt'><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>Реєстраційний номер облікової картки платника податків<br>
  або серія (за наявності) та номер паспорта<sup>1</sup><o:p></o:p></span></p>
  </td>
  <td width="40%" valign=top style='width:40.46%;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:white;padding:5.65pt 0cm 5.65pt 2.85pt;height:3.0pt'>
  <div align=right>
  <table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
   style='border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
   mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt'>
   <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;mso-yfti-lastrow:yes'>
    <td valign=top style='border:solid windowtext 1.0pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>1<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>2<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>3<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>4<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>5<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>6<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>7<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>8<o:p></o:p></span></p>
    </td>
    <td valign=top style='border:solid windowtext 1.0pt;border-left:none;
    mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
    padding:0cm 5.4pt 0cm 5.4pt'>
    <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
    text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
    letter-spacing:-.1pt;mso-fareast-language:UK'>8<o:p></o:p></span></p>
    </td>
   </tr>
  </table>
  </div>
  <p class=MsoNormal align=right style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:right;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><b><span
style='color:black;mso-fareast-language:UK'><span
style='mso-spacerun:yes'> </span></span></b><span style='color:black;
mso-fareast-language:UK'><o:p></o:p></span></p>

<table class=MsoNormalTable border=0 cellspacing=0 cellpadding=0 width="100%"
 style='width:100.0%;border-collapse:collapse;mso-yfti-tbllook:160;mso-padding-alt:
 0cm 0cm 0cm 0cm'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:3.0pt'>
  <td width="100%" valign=top style='width:100.0%;border:solid black 1.0pt;
  background:white;padding:2.85pt 2.85pt 2.85pt 2.85pt;height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><b><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>Ця частина декларації заповнюється
  посадовими особами контролюючого органу</span></b><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:3.0pt'>
  <td width="100%" valign=top style='width:100.0%;border:solid black 1.0pt;
  border-top:none;background:white;padding:8.5pt 2.85pt 8.5pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-bottom:0cm;margin-bottom:.0001pt;
  text-align:center;mso-line-height-alt:8.95pt'><span style='color:black;
  letter-spacing:-.1pt;mso-fareast-language:UK'>Відмітка про внесення даних до електронної
  бази податкової звітності<span style='mso-spacerun:yes'>              
  </span>«</span><span style='color:black;letter-spacing:-.6pt;mso-fareast-language:
  UK'>____</span><span style='color:black;letter-spacing:-.1pt;mso-fareast-language:
  UK'>» </span><span style='color:black;letter-spacing:-.6pt;mso-fareast-language:
  UK'>____________</span><span style='color:black;letter-spacing:-.1pt;
  mso-fareast-language:UK'> 20</span><span style='color:black;letter-spacing:
  -.6pt;mso-fareast-language:UK'>___</span><span style='color:black;letter-spacing:
  -.1pt;mso-fareast-language:UK'> року<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:3.0pt'>
  <td width="100%" valign=top style='width:100.0%;border:solid black 1.0pt;
  border-top:none;background:white;padding:2.85pt 2.85pt 8.5pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal align=center style='margin-top:.85pt;margin-right:0cm;
  margin-bottom:0cm;margin-left:0cm;margin-bottom:.0001pt;text-align:center;
  mso-line-height-alt:7.5pt'><i><span style='color:black;mso-fareast-language:
  UK'>(посадова особа контролюючого органу (підпис, ініціали та прізвище))</span></i><span
  style='color:black;mso-fareast-language:UK'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;mso-yfti-lastrow:yes;height:3.0pt'>
  <td width="100%" valign=top style='width:100.0%;border:solid black 1.0pt;
  border-top:none;background:white;padding:5.65pt 2.85pt 5.65pt 2.85pt;
  height:3.0pt'>
  <p class=MsoNormal style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;
  margin-left:14.15pt;margin-bottom:.0001pt;mso-line-height-alt:8.95pt'><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'>«</span><span
  style='color:black;letter-spacing:-.6pt;mso-fareast-language:UK'>____</span><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'>» </span><span
  style='color:black;letter-spacing:-.6pt;mso-fareast-language:UK'>____________</span><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'> 20</span><span
  style='color:black;letter-spacing:-.6pt;mso-fareast-language:UK'>___</span><span
  style='color:black;letter-spacing:-.1pt;mso-fareast-language:UK'> року<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;text-align:
justify;text-indent:14.15pt;mso-line-height-alt:9.65pt;background:white'><o:p>&nbsp;</o:p></p>

</div>

</body>

</html>

    """

    directory = "C:/Users/PC/Desktop/GIT/Kursova-PIS/Data/accountingForm/"
    os.makedirs(directory, exist_ok=True)

    file_name = f"{current_date}_{name}_податкова_форма3.html"
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)
        return True