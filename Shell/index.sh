#! /bin/bash
# ECHO COMMAND
echo UFT;
echo UFT FILE OPENER;


TFFN() {
  read -p "FileName:" FILENAME
  read -p "file name is $FILENAME (Y/n):" TFFN
  return "TFFN 1* - TFFN 2!"
}
if ["$TFFN"=="Y"]
then
  echo "TFFN 1* TFFN 
  
  while read line; do
# reading each line
echo $line
done < $filename2*" 
else
  TFFN
fi


while read line; do
  # reading each line
  echo $line
  done < $FILENAME
  
# now we have to give arg to linux command shell
