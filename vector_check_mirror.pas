program vector_check_mirror;
const m = 8;

var
  a: array [1..m] of integer;
  i, j: integer;
  mirror: boolean;

begin
  mirror:=true;
  for i:=1 to m do
    a[i] := 0;
  write('Enter the elements of the array: ');
  for i:=1 to m do
    read(a[i]);
  
    
  i:=1;
  j:=m;
  while i < j do
  begin
    if a[i]<>a[j] then mirror:=false;
    i:=i+1;
    j:=j-1;
  end;
  write('Вектор читається ');
  if mirror then writeln('oднаково')
    else writeln('не oднаково');

end.
