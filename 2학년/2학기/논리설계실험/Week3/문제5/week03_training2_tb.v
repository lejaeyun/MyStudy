module week03_training2_tb;

reg [9:0] A;
reg [9:0] B;
wire [4:0] Sum;

week03_training2
 U0 (
  .A(A),
  .B(B),
  .Sum(Sum));

  initial
  begin
    A = 10'b0000000000;
    #100 A = 10'b0000000100;
    #100 A = 10'b0000000100;
    #100 A = 10'b0000001000;
    #100 A = 10'b0000010000;
    #100 A = 10'b0000000000;
  end

  initial
  begin
    B = 10'b0000000000;
    #100 B = 10'b1000000000;
    #100 B = 10'b0001000000;
    #100 B = 10'b0000100000;
    #100 B = 10'b0000001000;
    #100 B = 10'b0000000000;
  end

endmodule
