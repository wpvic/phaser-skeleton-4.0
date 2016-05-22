// By ViTakahashi
var mainMenu = function(){}

mainMenu.prototype = {

	create:function(){
		// BG COLOR
		this.game.stage.backgroundColor = BG_COLOR
		// holds all animated text: no need to touch this
		this.all_to_be_animated_text_entities = []

		var w = this.game.width
		var h = this.game.height

		// Title
		var logo = this.game.add.bitmapText(w/2, -100, 'fontUsed', '', 75)
		logo.text = 'Pixel Plane'
		logo.anchor.setTo(0.5, 0.5)
		this.game.add.tween(logo).to({ y: h/2-80 }, 1000, Phaser.Easing.Bounce.Out).start()

		// Help
		var label = this.game.add.bitmapText(w/2, h-100, 'fontUsed', '', 40);
		label.text = 'Tap to control the plane'
		label.anchor.setTo(0.5, 0.5)
		label.alpha = 0
		this.game.add.tween(label).delay(500).to({ alpha: 1}, 1000).start()
		this.game.add.tween(label).to({y: h-120}, 500).to({y: h-100}, 500).loop().start()

		// touch input
		this.game.input.onDown.add( listener, this)

		function listener(game)
		{
			this.game.state.start('play')
		}
	},

	update:function()
	{		

		for(var i=0; i<this.all_to_be_animated_text_entities.length;i++)
		{
			// animateFontSize(text_item_from_all_to_be_animated_text_entities, max_size, min_size, size_change_rate=1)
			var max_size = this.all_to_be_animated_text_entities[i][2]
			var min_size = this.all_to_be_animated_text_entities[i][3]
			this.animateFontSize(this.all_to_be_animated_text_entities[i], max_size, min_size,1)
		}
	}
}