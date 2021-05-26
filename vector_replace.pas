program vector_replace;
const m = 8;
 
var 
  a: array [1..m] of integer;
  i: integer;

begin
  write('Enter the elements of the array: ');
  for i:=1 to m do
    read(a[i]);
  write('Print the elements:     ');
  for i:=1 to m do
    begin
      write(a[i],' ');
      if a[i] > 0 then
      begin
        a[i] := 1
      end
      else if a[i] < 0 then
      begin
        a[i] := -1
      end
    end;
  writeln('');
  write('Print the new elements: ');
  for i:=1 to m do
    begin
      write(a[i],' ');
    end;
  writeln('');
end.
