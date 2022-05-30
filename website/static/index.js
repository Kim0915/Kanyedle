var audio = document.getElementById("songAudio");


function pauseSong() {
    audio.pause();
}

function play_song(time){
    audio.currentTime = 0;
    audio.loop = true;
    audio.play();
    setTimeout(() => { audio.pause(); }, time);
    
}

function get_song(){
    console.log("Hello");
}