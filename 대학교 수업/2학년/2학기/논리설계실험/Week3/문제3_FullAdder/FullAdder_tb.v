module FullAdder_tb;

reg A;
reg B;
reg C;
wire Cout;
wire S;

Full_Adder
 U0 (
  .A(A),
  .B(B),
  .C(C),
  .Cout(Cout),
  .S(S));

  initial
  begin
    A = 1'b0;
    #400 A = 1'b1;
    #400 A = 1'b0;
  end

  initial
  begin
    B = 1'b0;
    #200 B = 1'b1;
    #200 B = 1'b0;
    #200 B = 1'b1;
    #200 B = 1'b0;
  end

  initial
  begin
    C = 1'b0;
    #100 C = 1'b1;
    #100 C = 1'b0;
    #100 C = 1'b1;
    #100 C = 1'b0;
    #100 C = 1'b1;
    #100 C = 1'b0;
    #100 C = 1'b1;
    #100 C = 1'b0;
  end

endmodule
