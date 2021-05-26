program vector_compare;
const m = 8;
 
var 
  a: array [1..m] of integer;
  i: integer;
  k: integer;
  cnt: integer;


begin
  for i:=1 to m do
    a[i] := 0;
  cnt := 0;
  write('Enter the elements of the array: ');
  for i:=1 to m do
    read(a[i]);
  write('Enter the k: ');
  read(k);
  write('Print the elements:    ');
  for i:=1 to m do
    begin
      write(a[i],' ');
      if a[i] = k then
      begin
        cnt := cnt + 1;
      end
    end;
  writeln('');
  write('The number of elements equal to k is: ');
  writeln(cnt);

end.
