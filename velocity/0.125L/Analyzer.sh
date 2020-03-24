#############################################
# This code is intended to analyze everything from the Measurement run 
#############################################

dir=$(dirname $0) #to get the directory where the script and other source files are.

echo "Analyzing the trajectory File"
echo "##########################################################################"
bash $dir/1Trajectory_Splitter.sh trajectory.xyz
python $dir/1Trajectory_Analizer.py
printf "\nGenerated 1Trajectory.xyz and Zshift.dat \n"

printf "\n##########################################################################\n"
echo "Analyzing the Chunk properties"
echo "##########################################################################"


printf "\n**************************************************************************\n"
echo "Analyzing the Solute properties"
echo "**************************************************************************"
bash $dir/Chunk_Splitter.sh Sproperties.all
python $dir/Chunk_Analyzer.py
mv Averages.dat SAverages.dat
for f in *.chunk;do mv "$f" "$f"s;done  #To rename as .chunks to analyze afterwards with Force_Factor.py

printf "\nGenerated SAverages.dat  \n"

printf "\n**************************************************************************\n"
echo "Analyzing the Solvent properties"
echo "**************************************************************************"
bash $dir/Chunk_Splitter.sh Lproperties.all
python $dir/Chunk_Analyzer.py
mv Averages.dat LAverages.dat

printf "\nGenerated LAverages.dat  \n"

printf "\n**************************************************************************\n"
echo "Analyzing the Fluid properties"
echo "**************************************************************************"
bash $dir/Chunk_Splitter.sh properties.all
python $dir/Chunk_Analyzer.py
mv Averages.dat AAverages.dat


printf "\nGenerated AAverages.dat \n"


rm *.chunk* 



