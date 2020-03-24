FILENAME=="mtt.lt"{print $0};
FILENAME=="mt.c"&&FNR>=1{
if ($1~/^Sol/) {
NW=substr($1,4);
#print NW
if (NW+0<=NWT) {
print $0;
}
}else{
print $0;
}
}
