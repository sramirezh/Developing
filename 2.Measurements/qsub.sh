#PBS -N YW_measure
#PBS -q long
#PBS -l walltime=02:00:00:00 
#PBS -l nodes=1:ppn=16
#PBS -M sr802@cam.ac.uk
#PBS -m ae
#PBS -j oe 

cd ${PBS_O_WORKDIR}
echo Starting job $PBS_JOBID 
echo
echo PBS assigned me this node: 
cat $PBS_NODEFILE 
echo 
echo "Running ${job_name}" 
echo 

mpirun -np 16 /home/sr802/lammps-31Mar17/src/lmp_dexter -in measure.lmp
wait 
mkdir stress_dir 
cp properties.all stress
mv stress stress_dir 
cd stress_dir 
python ~/python_modules/comment_timesteps.py stress 
cd .. 

wait 
mkdir A_dir 
cp Lproperties.all A
mv A A_dir 
cd A_dir 
python ~/python_modules/comment_timesteps.py A 
cd .. 

wait 
mkdir B_dir 
cp Sproperties.all B
mv B B_dir 
cd B_dir 
python ~/python_modules/comment_timesteps.py B 
cd .. 

echo 
echo "Job finished. PBS details are:" 
echo 
qstat -f ${PBS_JOBID} 
echo 
echo Finished at \`date\` 
