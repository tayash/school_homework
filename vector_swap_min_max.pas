program vector_swap_min_max;
const m = 8;

var
  a: array [1..m] of integer;
  i_min, i_max: integer;
  i: integer;
  x: integer;


begin
  for i:=1 to m do
    a[i] := 0;
  write('Enter the elements of the array: ');
  for i:=1 to m do
    read(a[i]);
  i_min:=1;
  i_max:=1;


  for i:=1 to m do
    begin
      if a[i]<a[i_min] then i_min:=i;
      if a[i]>a[i_max] then i_max:=i;
    end;
  write('i_min=');
  writeln(i_min);
  write('i_max=');
  writeln(i_max);
  x:=a[i_min];
  a[i_min]:=a[i_max];
  a[i_max]:=x;
  for i:=1 to m do
    begin
    writeln(a[i]);
    end;

end.
