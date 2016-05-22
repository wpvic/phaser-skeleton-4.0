var boot = function(){console.log('Commencing game...')}

boot.prototype = 
{
	preload:function(){
		this.game.load.image('loading', 'assets/loading_x1.png')
	},
	create:function(){

		this.game.plugins.screenShake = this.game.plugins.add(Phaser.Plugin.ScreenShake)
		this.scale.scaleMode = Phaser.ScaleManager.SHOW_ALL

		if(this.isDeviceMobile()) // if mobile
		{
			// using outerWidth fixes the scaling problem in mobile devices. FINALLY SOLVED THIS CRAP!
			this.scale.minWidth = window.outerWidth
			this.scale.minHeight = window.outerHeight
			this.scale.maxWidth = window.outerWidth
			this.scale.maxHeight = window.outerHeight
		}
		else // if on computer
		{
			this.scale.minWidth = 320
			this.scale.minHeight = 480
			this.scale.maxWidth = 450
			this.scale.maxHeight = 600
		}
		this.scale.pageAlignHorizontally = true
		this.scale.pageAlignVertically = true
		this.scale.setScreenSize = true
		this.game.state.start('preload')
	},
	isDeviceMobile:function()
	{
		var isMobile = {
		    Android: function() {
		        return navigator.userAgent.match(/Android/i);
		    },
		    BlackBerry: function() {
		        return navigator.userAgent.match(/BlackBerry/i);
		    },
		    iOS: function() {
		        return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		    },
		    Opera: function() {
		        return navigator.userAgent.match(/Opera Mini/i);
		    },
		    Windows: function() {
		        return navigator.userAgent.match(/IEMobile/i);
		    },
		    any: function() {
		        return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		    }
		}
		return isMobile.any()
	}
}
