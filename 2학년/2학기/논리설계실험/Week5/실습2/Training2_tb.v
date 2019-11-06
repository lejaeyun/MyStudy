module Training2_tb;

reg [9:0] Dec;
reg RST;
wire [4:0] Sum;

Training2
 U0 (
  .Dec(Dec),
  .RST(RST),
  .Sum(Sum));

  initial
  begin
    Dec = 10'b0000000000;
    #400 Dec = 10'b0000000100;
    #100 Dec = 10'b0000000000;
    #100 Dec = 10'b0000010000;
    #100 Dec = 10'b0000000000;
  end

  initial
  begin
    RST = 1'b1;
    #100 RST = 1'b0;
  end

endmodule
