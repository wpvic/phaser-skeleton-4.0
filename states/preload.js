var preload = function(){}

preload.prototype = {
	preload:function(){

		this.game.stage.backgroundColor = BG_COLOR

		var loading = this.add.sprite(this.game.width/2,this.game.height/2,'loading')
		loading.anchor.setTo(.5,.5)
		loading.scale.setTo(.6,.3)
		this.load.setPreloadSprite(loading)
		
		// game entities/world
		this.load.image('player', 'assets/player_x1.png')
		this.load.image('obstacle', 'assets/obstacle_x2.png')

		// icons
		this.load.image('pause', 'assets/pause.png')

		// audio
		this.load.audio('bg_spin', 'sounds/spin_bg_music.mp3')
		this.load.audio('bg_edm', 'sounds/edm_bg_music.mp3')
		this.load.audio('score', 'sounds/score.wav')
		this.load.audio('kill', 'sounds/kill.ogg')

		// font
		this.game.load.bitmapFont('fontUsed', 'font/ganonwhite/font.png', 'font/ganonwhite/font.xml');

	},
	create:function(){
		this.game.state.start('mainMenu')
	}
}