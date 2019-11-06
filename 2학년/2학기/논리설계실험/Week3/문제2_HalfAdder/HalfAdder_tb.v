module HalfAdder_tb;

reg A;
reg B;
wire C;
wire S;

half_adder
 U0 (
  .A(A),
  .B(B),
  .C(C),
  .S(S));

  initial
  begin
    A = 1'b0;
    #100 A = 1'b1;
    #100 A = 1'b0;
    #100 A = 1'b0;
    #100 A = 1'b0;
    #100 A = 1'b1;
    #100 A = 1'b0;
  end

  initial
  begin
    B = 1'b0;
    #100 B = 1'b0;
    #100 B = 1'b0;
    #100 B = 1'b1;
    #100 B = 1'b0;
    #100 B = 1'b1;
    #100 B = 1'b0;
  end

endmodule
