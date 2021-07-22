package KoalaBot.KoalaBot.commands;

import com.jagrosh.jdautilities.command.Command;
import com.jagrosh.jdautilities.command.CommandEvent;

public class Bestflip extends Command{
	public Bestflip() {
		this.name = "Bestflip";
		this.help = "Get current best flip";
	}
	@Override
	protected void execute(CommandEvent e) {
		e.reply("Test");
	}

}
