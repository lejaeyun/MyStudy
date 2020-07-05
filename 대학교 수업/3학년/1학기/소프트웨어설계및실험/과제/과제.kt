import java.util.Random

class score() {
    var myscore:Array<Int> = Array<Int>(10, {0})
    fun scorein(index:Int, value:Int) {
        myscore[index-1] = myscore[index-1] + value
    }
    
}

class dice() {
    var max : Int = 10
    set(value) {
        var random = Random()
        field = random.nextInt(value)+1
    }
    get() {
        return field
    }
    
}

fun main() {
    var pre : Int = -1
    var plusscore : Int
    var mydice = dice()
    var myscore = score()
    for (i in 1..20) {
    	mydice.max = 10
    	if (pre == mydice.max) {
            plusscore = 10
        }
        else {
            plusscore = 1
        }
        myscore.scorein(mydice.max, plusscore)
        pre = mydice.max
	}
    
    for (i in 1..10) {
        print("now index : ")
        println(i)
        println(myscore.myscore[i-1])
	}
}