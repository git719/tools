#!/usr/bin/awk -f
# csv2html.awk

BEGIN {
    FS=",";
    print "<html>";
    print "<head>";
    print "<style>";
    print "h1, h5, th { text-align: center; font-family: Segoe UI; }";
    print "table { margin: auto; font-family: Segoe UI; box-shadow: 10px 10px 5px #888; border: thin ridge grey; }";
    print "th { background: #0046c3; color: #fff; max-width: 400px; padding: 5px 10px; }";
    print "td { font-size: 11px; padding: 5px 20px; color: #000; }";
    print "tr { background: #b8d1f3; }";
    print "tr:nth-child(even) { background: #dae5f4; }";
    print "tr:nth-child(odd) { background: #b8d1f3; }";
    print "</style>";
    print "</head>";
    print "<body><table>"

}

function printRow(tag) {
    print "<tr>";
    for (i=1; i<=NF; i++)
        print "<"tag">"$i"</"tag">";
    print "</tr>"
}

NR==1 {
    printRow("th")
}

NR>1 {
    printRow("td")
}

END {
    print "</table></body></html>"
}
