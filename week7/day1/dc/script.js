class video {
    constructor (title,uploader,time){
        this.title = title
        this.uploader = uploader
        this.time = time
    }
    watch(){
        console.log(`${this.uploader} watched all ${this.time} seconds of ${this.title}!`);
      }
    }

    const video1 = new Video ("Introduction to JavaScript", "JohnDoe", 300);

    video1.watch();
    
    const video2 = new Video("Avanced JS", "DavidJoe", 500);
    
    video2.watch();