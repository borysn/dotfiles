###########
# exports #
###########
export JAVA_HOME=/opt/oracle-jdk-bin-1.8.0.121
export TERMINAL=urxvt

########
# aias #
########
# firefox theme
alias firefox="env GTK_THEME=Adwaita:light firefox"

###################
# nvidia settings #
###################
nvidia-settings --assign CurrentMetaMode="nvidia-auto-select +0+0 { ForceFullCompositionPipeline = On }"
nvidia-settings -a '[gpu:0]/GPUPowerMizerMode=1'

##########
# sdkman #
##########
#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/p3pt/.sdkman"
[[ -s "/home/p3pt/.sdkman/bin/sdkman-init.sh" ]] && source "/home/p3pt/.sdkman/bin/sdkman-init.sh"
