const $guessForm = $("#guessForm")
const $guess = $("#guess")
const $answer = $('#answer')
const $score = $('#score')
const $timer = $('#timer')
const $reset = $('#reset')
const $gamesPlayed = $('#gamesPlayed')

async function checkGuess(guess){
    const res = await axios.get(`guess/${guess}`)

    return res;
}

async function postResults(score){
    const post = await axios.post(`post/${score}`)
}

if($timer != undefined){
    function decreaseTime(){
        if(parseInt($timer[0].innerText) > 0){
            $timer[0].innerText = parseInt($timer[0].innerText) - 1
            console.log('decreasedTime()')
        } else {
            clearInterval(timer)
        }
    }
    
    let timer = setInterval(() => {
        decreaseTime()
        }, 1000)
}

const usedWords = []

$guessForm.on('submit', async function handleGuess(evt) {
    let guess = $guess.val().toLowerCase();
    if(parseInt($timer[0].innerText) > 0 && !usedWords.includes(guess)){
        evt.preventDefault();
        let val = $guess.val().toLowerCase();

        res = await checkGuess(val);
        console.log(res)
        
        if(res.data == 'ok'){
            $answer[0].innerText = 'Good guess!'
            $score[0].innerText = parseInt($score[0].innerText) + 1
            usedWords.push(guess)
        } else{
            $answer[0].innerText = res.data
            usedWords.push(guess)
        }
    } else if(parseInt($timer[0].innerText) <= 0){
        evt.preventDefault()
        $answer[0].innerText = 'Out of time!'
    } else {
        evt.preventDefault()
        $answer[0].innerText = 'Already guessed that word'
    }
})

// if(parseInt($timer[0].innerText) > 0){
//     console.log('while')
// } 

$reset.on('click', function(evt){
    evt.preventDefault()
    postResults(parseInt($score[0].innerText))
})


