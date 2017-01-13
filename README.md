# SHA3
Investigation into SHA 3 vulnerabilities


##Theta Function
<p> 

3D matrix implementation of theta function, includes generate function which generates 5 x 5 x w matrix of random 1's and 0's
</p>

##Matrix Utils 

<p>
Matrix print functions <br />
</p>
###Use:
<p>
Use of the matPrint function is recommended: <br />
    <b>matPrint(mat, format, comp, label, *args):</b>
<br />    
Prints a matrix by row, column, or lane
<br />
<br />
variables: 
<ul>
   <li>mat = the matrix to print</li>
   <li>format = r, c, or l to prints rows, columns or lanes respectively</li>
   <li>comp = boolean states whether to compare matrix mat with another matrix supplied as the final argument</li>
   <li>label = boolean states whether or not to label to output</li>
   <li>*args = where the comparison matrix is supplied </li>
</ul>
</p>
<b>Example:</b>
```
    matPrint(Ap, 'c', True, True, A)
```
Will print Ap column by column compared with A and labeled 


