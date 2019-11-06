module HundredCounter_tb;

wire [3:0] CNT10;
wire [3:0] CNT100;
reg clk;
reg rst;

HundredCounter
 U0 (
  .CNT10(CNT10),
  .CNT100(CNT100),
  .clk(clk),
  .rst(rst));

  initial
  begin
    clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
    #100 clk = 1'b0;
    #100 clk = 1'b1;
  end

  initial
  begin
    rst = 1'b0;
    #100 rst = 1'b1;
    #200 rst = 1'b0;
  end

endmodule
