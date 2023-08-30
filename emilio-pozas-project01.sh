hostname

names="John Doe;Bill Withers;Arthur Morgan;Mary Jane;Rick Ross;John Marston"
echo $names | cut -d ';' -f 3
echo $names | cut -d ';' -f 6