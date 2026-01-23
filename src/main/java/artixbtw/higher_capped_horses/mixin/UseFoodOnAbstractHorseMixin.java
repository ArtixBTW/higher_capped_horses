package artixbtw.higher_capped_horses.mixin;

import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.animal.equine.AbstractHorse;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.Level;

@Mixin(Item.class)
public class UseFoodOnAbstractHorseMixin {
	@Inject(at = @At("head"), method = "use", cancellable = true)
	public void use(
			Level level,
			Player player,
			InteractionHand hand,
			CallbackInfoReturnable<InteractionResult> cir) {
		ItemStack stack = player.getItemInHand(hand);
		if (player.getRootVehicle() instanceof AbstractHorse abstractHorse
				&& abstractHorse.isFood(stack)) {
			InteractionResult result = abstractHorse.fedFood(player, stack);
			cir.setReturnValue(result);
		}
	}
}
