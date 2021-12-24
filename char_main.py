


class char():
    def __init__( self, name, base_hp, base_attack, base_def, crit_multi, crit_chance, base_dmg_increase,
                  skill_damage, energy_recharge, elemental_mastery):
        self.name = name
        self.crit_chance = crit_chance
        self.base_dmg_increase = base_dmg_increase
        self.base_def = base_def
        self.crit_multi = crit_multi
        self.base_attack = base_attack
        self.base_hp = base_hp
        self.skill_damage = skill_damage
        self.weapon_multiplier = 0
        self.native_damage_bonus = 0
        self.attack_increasement = 0
        self.energy_recharge = energy_recharge
        self.elemental_mastery = elemental_mastery
        self.additional_hp = 0
        self.additional_def = 0
        self.additional_atk = 0
        self.react_multi = 100
    def dmg_calculation(self):
        #self.all_artifacts_adds(faq_list)
        self.all_myltipliers_activation()
        if self.crit_chance > 100:
            self.crit_chance = 100
        non_crit_final_skill_damage = (self.base_attack * (1 + self.attack_increasement / 100) + self.additional_atk) * \
                             ((100 + self.native_damage_bonus) / 100) * \
                             self.skill_damage / 100 * \
                             ((100 + self.weapon_multiplier) / 100) * self.react_multi / 100
        crit_final_skill_damage = non_crit_final_skill_damage * (self.crit_multi + 100) / 100
        final_skill_damag = non_crit_final_skill_damage * (1 + self.crit_chance * self.crit_multi / 10000)
        #print(non_crit_final_skill_damage,"non-crit")
        #print(crit_final_skill_damage, "crit")
        self.all_myltipliers_deactivation()
        return final_skill_damag
    def add_weapon(self,added_weapon):
        self.attack_increasement += added_weapon.weapon_attack_increasement
        self.base_def += added_weapon.weapon_def
        self.crit_multi += added_weapon.crit_multi
        self.base_hp += added_weapon.weapon_hp
        self.crit_chance += added_weapon.crit_chance
        self.weapon_multiplier += added_weapon.weapon_multiplier
        self.base_attack += added_weapon.weapon_base_attack
        self.native_damage_bonus += added_weapon.native_damage_bonus_increasement
        self.elemental_mastery += added_weapon.weapon_elemental_mastery
        self.energy_recharge += added_weapon.weapon_energy_recharge
        # self... += added_weapon...
#reactions
    def first_react_active(self):
        self.react_multi += 1 + (278 * self.elemental_mastery / (1400 + self.elemental_mastery))
    def first_react_deactive(self):
        self.react_multi -= 1 + (278 * self.elemental_mastery / (1400 + self.elemental_mastery))
#additional options
    def hu_tao_active(self):
        # e-skill lvl 10 activation
        if (self.base_hp + self.additional_hp) * 0.0626 <= self.base_attack * 4:
            self.additional_atk += (self.base_hp + self.additional_hp) * 0.0626
        else:
            self.additional_atk += self.base_attack * 4
            print("base atck is too law for your hp")
        # passive skill activation
        self.native_damage_bonus += 33
    def hu_tao_deactive(self):
        # e-skill lvl 10 activation
        if (self.base_hp + self.additional_hp) * 0.0626 <= self.base_attack * 4:
            self.additional_atk -= (self.base_hp + self.additional_hp) * 0.0626
        else:
            self.additional_atk -= self.base_attack * 4
            print("base atck is too law for your hp")
        # passive skill activation
        self.native_damage_bonus -= 33
    def epos_active(self):
        self.attack_increasement += 48
    def epos_deactive(self):
        self.attack_increasement -= 48
    def cdz_active(self):
        self.attack_increasement += 20
    def cdz_deactive(self):
        self.attack_increasement -= 20
#system
    def all_myltipliers_activation(self):
        self.activation_list = [first_react_active,cdz_active,epos_active,hu_tao_active]
        if first_react_active == 1:
            self.first_react_active()
        if cdz_active == 1:
            self.cdz_active()
        if epos_active == 1:
            self.epos_active()
        if hu_tao_active == 1:
            self.hu_tao_active()
    def all_myltipliers_deactivation(self):
        self.activation_list = [first_react_active,cdz_active,epos_active,hu_tao_active]
        if first_react_active == 1:
            self.first_react_deactive()
        if cdz_active == 1:
            self.cdz_deactive()
        if epos_active == 1:
            self.epos_deactive()
        if hu_tao_active == 1:
            self.hu_tao_deactive()
    def all_artifacts_main_stat_activation(self,faq_list):
        self.additional_hp += 4780
        self.additional_atk += 311
        self.crit_chance += faq_list[0][1]
        self.crit_multi += faq_list[1][1]
        self.attack_increasement += faq_list[2][1]
        self.elemental_mastery += faq_list[4][1]
        self.additional_hp += (self.base_hp * faq_list[5][1] / 100)
        self.native_damage_bonus += faq_list[6][1]
#artifacts manipulation
    def check_sub_stat_suport_function(self, stat):
        self.sub_stat = stat
        self.return_value = self.dmg_calculation()
        if self.sub_stat == 'crit_chance':
            self.crit_chance += 3.5
            if self.crit_chance > 100:
                self.crit_chance -= 3.5
                self.return_value = self.dmg_calculation()
            else:
                self.return_value = self.dmg_calculation()
                self.crit_chance -= 3.5
        if self.sub_stat == 'attack_flat':
            self.additional_atk += 17.51
            self.return_value = self.dmg_calculation()
            self.additional_atk -= 17.51
        if self.sub_stat == 'life_flat':
            self.additional_hp += 268.88
            self.return_value = self.dmg_calculation()
            self.additional_hp -= 268.88
        if self.sub_stat == 'attack_increas':
            self.attack_increasement += 5.25
            self.return_value = self.dmg_calculation()
            self.attack_increasement -= 5.25
        if self.sub_stat == 'elemental_mastery':
            self.elemental_mastery += 20.98
            self.return_value = self.dmg_calculation()
            self.elemental_mastery -= 20.98
        if self.sub_stat == 'crit_multi':
            self.crit_multi += 7
            self.return_value = self.dmg_calculation()
            self.crit_multi -= 7
        if self.sub_stat == 'life_increas':
            self.additional_hp += 0.0525 * self.base_hp
            self.return_value = self.dmg_calculation()
            self.additional_hp -= 0.0525 * self.base_hp
        return self.return_value
    def check_sub_stat(self):
        dmg_list = []
        for i in range(1):
            stats_list = [
                'crit_chance',
                'crit_multi',
                'attack_increas',
                'attack_flat',
                'elemental_mastery',
                'life_increas',
                'life_flat']
            for i in range(len(stats_list)):
                item = self.check_sub_stat_suport_function(stats_list[i])
                dmg_list.append({stats_list[i] : item})
        self.highest = dmg_list[0]
        for i in range(len(stats_list)-1):
            value_to_work_with = sum(list(self.highest.values()))
            if dmg_list[i].get(stats_list[i]) >= value_to_work_with:
                self.highest = dmg_list[i]
        return self.highest
    def add_sub_stat(self,highest,list_to_work_with):
# highest is a dict in form {{'crit_chance': 21489.630052429842}}|damage after changes|
        self.highest = highest
        self.sub_stat = list(self.highest.keys())[0]#to get 'crit_chance'
        #self.value_to_work_with = sum(list(self.highest.values()))
        for i in range(len(sub_stats_list)):
            if self.sub_stat == sub_stats_list[i][0] and self.sub_stat:
                sub_stats_list[i][1] += 1
                list_to_work_with[i][1] += 1
        if self.sub_stat == 'crit_chance':
            self.crit_chance += 3.5
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'attack_flat':
            self.additional_atk += 17.51
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'life_flat':
            self.additional_hp += 268.88
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'attack_increas':
            self.attack_increasement += 5.25
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'elemental_mastery':
            self.elemental_mastery += 20.98
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'crit_multi':
            self.crit_multi += 7
            self.return_value = self.dmg_calculation()
        if self.sub_stat == 'life_increas':
            self.additional_hp += 0.0525 * self.base_hp
            self.return_value = self.dmg_calculation()
# fill sub stat list with new number of sub stuts in form [['crit_chance', 1], ['crit_multi', 0], ['attack_increas', 0], ['attack_flat', 0], ['elemental_mastery', 0], ['life_increas', 0], ['life_flat', 0]]
        return list_to_work_with
class weapon():
    def __init__(self, name, weapon_base_attack, weapon_multiplier, weapon_hp, weapon_def, weapon_attack_increasement,
                 crit_multi, crit_chance, native_damage_bonus_increasement, weapon_elemental_mastery, weapon_energy_recharge):
        self.name = name
        self.weapon_base_attack = weapon_base_attack
        self.weapon_multiplier = weapon_multiplier
        self.weapon_hp = weapon_hp
        self.weapon_def = weapon_def
        self.weapon_attack_increasement = weapon_attack_increasement
        self.crit_multi = crit_multi
        self.crit_chance = crit_chance
        self.native_damage_bonus_increasement = native_damage_bonus_increasement
        self.weapon_elemental_mastery = weapon_elemental_mastery
        self.weapon_energy_recharge = weapon_energy_recharge

class artifact():

    def __init__(self, head_stat):
        self.head_stat = 0
        stats = []

#characters implementation
faq_list = [
        ['crit_chance', 31.1],
        ['crit_multi', 0],
        ['attack_increas', 46.6],
        ['attack_flat', 0],
        ['elemental_mastery', 0],
        ['life_increas', 0],
        ['life_flat', 0],
        ['native_damage_bonuse', 46.6]]
sub_stats_list = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
list_to_work_with_for_flower = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
list_to_work_with_for_pero = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
list_to_work_with_for_chasy = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
list_to_work_with_for_chaska = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
list_to_work_with_for_korona = [
                ['crit_chance', 0 ],
                ['crit_multi', 0],
                ['attack_increas', 0],
                ['attack_flat', 0],
                ['elemental_mastery', 0],
                ['life_increas', 0],
                ['life_flat', 0]]
hytao = char('hy tao charged attack', 15552, 106, 876, 88.4, 5, 0, 242.6, 100, 0)
eula = char('eula ulti c6 -_-', 13226, 342+627, 751, 88.4, 5, 0, 1466.76, 100, 0)
first_react_active = 0
hu_tao_active = 0
epos_active = 0
cdz_active = 0

#weapons
groza_drakonov = weapon( "groza drakonov", 454, 24, 0, 0, 0, 0, 0, 0, 221, 0)
semrtelny_boy = weapon( "smertelmy boy", 454, 0, 0, 16, 16, 0, 36.8, 0, 0, 0)
bpclaymore = weapon("bp claymore", 510, 30, 0, 0, 0, 0, 27.6, 0, 0, 0)
def run_character_calculation(charecter):
    print(charecter.dmg_calculation())
    for i in range(6):
        x = charecter.check_sub_stat()
        charecter.add_sub_stat(x, list_to_work_with_for_flower)
        x = charecter.check_sub_stat()
        charecter.add_sub_stat(x, list_to_work_with_for_chasy)
        x = charecter.check_sub_stat()
        charecter.add_sub_stat(x, list_to_work_with_for_chaska)
        x = charecter.check_sub_stat()
        charecter.add_sub_stat(x, list_to_work_with_for_korona)
        x = charecter.check_sub_stat()
        charecter.add_sub_stat(x, list_to_work_with_for_pero)
    print(list_to_work_with_for_flower)
    print(list_to_work_with_for_chaska)
    print(list_to_work_with_for_chasy)
    print(list_to_work_with_for_pero)
    print(list_to_work_with_for_korona)
    print(charecter.dmg_calculation())
    print(charecter.crit_chance)
    print(charecter.crit_multi)
def hytao_go():
    global first_react_active
    global hu_tao_active
    faq_list_for_hytao = [
        ['crit_chance', 31.1],
        ['crit_multi', 0],
        ['attack_increas', 0],
        ['attack_flat', 0],
        ['elemental_mastery', 270],
        ['life_increas', 0],
        ['life_flat', 0],
        ['native_damage_bonuse', 46.6]]
    hytao.add_weapon(groza_drakonov)
    #hytao.add_weapon(semrtelny_boy)
    hytao.all_artifacts_main_stat_activation(faq_list_for_hytao)
    first_react_active = 1
    hu_tao_active = 1
    run_character_calculation(hytao)
def eula_go():
    global cdz_active
    global epos_active
    epos_active = 0
    cdz_active = 1
    faq_list_for_eula = [
        ['crit_chance', 31.1],
        ['crit_multi', 0],
        ['attack_increas', 46.6],
        ['attack_flat', 0],
        ['elemental_mastery', 0],
        ['life_increas', 0],
        ['life_flat', 0],
        ['native_damage_bonuse', 46.6]]
    eula.add_weapon(bpclaymore)
    eula.all_artifacts_main_stat_activation(faq_list_for_eula)
    run_character_calculation(eula)

fill_the_list = True
buf_arts = False



#run part
eula_go()
#hytao_go()
