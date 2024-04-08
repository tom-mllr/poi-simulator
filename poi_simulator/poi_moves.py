from poi_simulator.utils import TimingDirection
from dataclasses import dataclass


@dataclass
class PoiMove:
    name: str
    l_prop_speed_factor: int
    l_prop_angle_offset: float
    l_arm_speed_factor: float
    l_arm_angle_offset: float
    r_prop_speed_factor: int
    r_prop_angle_offset: float
    r_arm_speed_factor: float
    r_arm_angle_offset: float



poi_moves = {}
poi_moves["1-Beat"] = {}

poi_moves = [
    # 1-Beat
    
    # Inspin
    PoiMove("Tog/Same Extension",                                                    1,  0.0,  1,  0.0,  1,  0.0,  1,  0),
    PoiMove("Tog/Opp Extension",                                                     1,  0.0,  1,  0.0, -1,  1.0, -1,  1),
    PoiMove("Split/Same Extension",                                                  1,  0.0,  1,  0.0,  1,  1.0,  1,  1),
    PoiMove("Split/Opp Extension",                                                   1,  0.0,  1,  0.0, -1,  0.0, -1,  0),

    # 2-Beat
    
    # Inspin Flowers
    PoiMove("Tog/Same Inspin Flower 1-Petal Left",                                     2,  0.0,  1,  0.0,  2,  0.0,  1,  0),
    PoiMove("Tog/Same Inspin Flower 1-Petal Right",                                    2,  1.0,  1,  0.0,  2,  1.0,  1,  0),
    PoiMove("Tog/Same Inspin Flower 1-Petal Top",                                      2,  1.5,  1,  0.0,  2,  1.5,  1,  0),
    PoiMove("Tog/Same Inspin Flower 1-Petal Bottom",                                   2,  0.5,  1,  0.0,  2,  0.5,  1,  0),
    
    PoiMove("Tog/Opp Inspin Flower 1-Petal Left/Right In",                             2,  1.0,  1,  0.0, -2,  0.0, -1,  1),
    PoiMove("Tog/Opp Inspin Flower 1-Petal Left/Right Out",                            2,  0.0,  1,  0.0, -2,  1.0, -1,  1),
    PoiMove("Tog/Opp Inspin Flower 1-Petal Top",                                       2,  1.5,  1,  0.0, -2,  1.5, -1,  1),
    PoiMove("Tog/Opp Inspin Flower 1-Petal Bottom",                                    2,  0.5,  1,  0.0, -2,  0.5, -1,  1),
    
    PoiMove("Split/Same Inspin Flower 1-Petal Left-Left/Right-Right",                          2,  0.0,  1,  0.0,  2,  1.0,  1,  1),
    PoiMove("Split/Same Inspin Flower 1-Petal Left-Right/Right-Left",                         2,  1.0,  1,  0.0,  2,  0.0,  1,  1),
    PoiMove("Split/Same Inspin Flower 1-Petal Left-Top/Right-Bottom",                  2,  0.5,  1,  0.0,  2,  1.5,  1,  1),
    PoiMove("Split/Same Inspin Flower 1-Petal Left-Bottom/Right-Top",                  2,  1.5,  1,  0.0,  2,  0.5,  1,  1),

    PoiMove("Split/Opp Inspin Flower 1-Petal Left",                                    2,  0.0,  1,  0.0, -2,  0.0, -1,  0),
    PoiMove("Split/Opp Inspin Flower 1-Petal Right",                                   2,  1.0,  1,  0.0, -2,  1.0, -1,  0),
    PoiMove("Split/Opp Inspin Flower 1-Petal Left-Top/Right-Bottom",                   2,  1.5,  1,  0.0, -2,  0.5, -1,  0),
    PoiMove("Split/Opp Inspin Flower 1-Petal Left-Bottom/Right-Top",                   2,  0.5,  1,  0.0, -2,  1.5, -1,  0),
    
    
    # Antispin Flowers
    PoiMove("Tog/Same Antispin Flower 3-Petal Left",                                   -2,  1.0,  1,  0.0, -2,  1.0,  1,  0),
    PoiMove("Tog/Same Antispin Flower 3-Petal Right",                                  -2,  0.0,  1,  0.0, -2,  0.0,  1,  0),
    PoiMove("Tog/Same Antispin Flower 3-Petal Up",                                     -2,  0.5,  1,  0.0, -2,  0.5,  1,  0),
    PoiMove("Tog/Same Antispin Flower 3-Petal Down",                                   -2,  1.5,  1,  0.0, -2,  1.5,  1,  0),
    
    PoiMove("Tog/Opp Antispin Flower 3-Petal Left-Left/Right-Right",                   -2,  1.0,  1,  0.0,  2,  0.0, -1,  1),
    PoiMove("Tog/Opp Antispin Flower 3-Petal Left-Right/Right-Left",                   -2,  0.0,  1,  0.0,  2,  1.0, -1,  1),
    PoiMove("Tog/Opp Antispin Flower 3-Petal Up",                                      -2,  0.5,  1,  0.0,  2,  0.5, -1,  1),
    PoiMove("Tog/Opp Antispin Flower 3-Petal Down",                                    -2,  1.5,  1,  0.0,  2,  1.5, -1,  1),
    
    PoiMove("Split/Same Antispin Flower 3-Petal Left-Right/Right-Left",                -2,  0.0,  1,  0.0, -2,  1.0,  1,  1),
    PoiMove("Split/Same Antispin Flower 3-Petal Left-Left/Right-Right",                -2,  1.0,  1,  0.0, -2,  0.0,  1,  1),
    PoiMove("Split/Same Antispin Flower 3-Petal Left-Up/Right-Down",                   -2,  0.5,  1,  0.0, -2,  1.5,  1,  1),
    PoiMove("Split/Same Antispin Flower 3-Petal Left-Down/Right-Up",                   -2,  1.5,  1,  0.0, -2,  0.5,  1,  1),
    
    PoiMove("Split/Opp Antispin Flower 3-Petal Left",                                  -2,  1.0,  1,  0.0,  2,  1.0, -1,  0),
    PoiMove("Split/Opp Antispin Flower 3-Petal Right",                                 -2,  0.0,  1,  0.0,  2,  0.0, -1,  0),
    PoiMove("Split/Opp Antispin Flower 3-Petal Left-Up/Right-Down",                    -2,  0.5,  1,  0.0,  2,  1.5, -1,  0),
    PoiMove("Split/Opp Antispin Flower 3-Petal Left-Down/Right-Up",                    -2,  1.5,  1,  0.0,  2,  0.5, -1,  0),
    
    
    # Hybrids
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin 1-Petal Left vs Antispin 3-Petal Left",          2,  0.0,  1,  0.0, -2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin 1-Petal Right vs Antispin 3-Petal Right",        2,  1.0,  1,  0.0, -2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin 1-Petal Bottom vs Antispin 3-Petal Up",          2,  0.5,  1,  0.0, -2,  0.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin 1-Petal Top vs Antispin 3-Petal Down",           2,  1.5,  1,  0.0, -2,  1.5,  1,  0),
    
    PoiMove("Arms Tog/Same Prop Tog/Opp Antispin 3-Petal Left vs Inspin 1-Petal Left",         -2,  1.0,  1,  0.0,  2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Antispin 3-Petal Right vs Inspin 1-Petal Right",       -2,  0.0,  1,  0.0,  2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Antispin 3-Petal Up vs Inspin 1-Petal Bottom",         -2,  0.5,  1,  0.0,  2,  0.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Tog/Opp Antispin 3-Petal Down vs Inspin 1-Petal Top",          -2,  1.5,  1,  0.0,  2,  1.5,  1,  0),
    
    PoiMove("Arms Tog/Same Prop Split/Same Inspin 1-Petal Left vs Inspin 1-Petal Right",        2,  0.0,  1,  0.0,  2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Inspin 1-Petal Right vs Inspin 1-Petal Right",       2,  1.0,  1,  0.0,  2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Inspin 1-Petal Bottom vs Inspin 1-Petal Top",        2,  0.5,  1,  0.0,  2,  1.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Inspin 1-Petal Top vs Inspin 1-Petal Bottom",        2,  1.5,  1,  0.0,  2,  0.5,  1,  0),

    PoiMove("Arms Tog/Same Prop Split/Same Antispin 3-Petal Left vs Antispin 3-Petal Right",   -2,  1.0,  1,  0.0,  -2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Antispin 3-Petal Right vs Antispin 3-Petal Left",   -2,  0.0,  1,  0.0,  -2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Antispin 3-Petal Up vs Antispin 3-Petal Down",      -2,  0.5,  1,  0.0,  -2,  1.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Same Antispin 3-Petal Down vs Antispin 3-Petal Up",      -2,  1.5,  1,  0.0,  -2,  0.5,  1,  0),
    
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin 1-Petal Left vs Antispin 3-Petal Right",       2,  0.0,  1,  0.0,  -2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin 1-Petal Right vs Antispin 3-Petal Right",      2,  1.0,  1,  0.0,  -2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin 1-Petal Bottom vs Antispin 3-Petal Top",       2,  0.5,  1,  0.0,  -2,  1.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin 1-Petal Top vs Antispin 3-Petal Bottom",       2,  1.5,  1,  0.0,  -2,  0.5,  1,  0),

    PoiMove("Arms Tog/Same Prop Split/Opp Antispin 3-Petal Left vs Inspin 1-Petal Right",      -2,  1.0,  1,  0.0,   2,  0.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Antispin 3-Petal Right vs Inspin 1-Petal Left",      -2,  0.0,  1,  0.0,   2,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Antispin 3-Petal Up vs Inspin 1-Petal Down",         -2,  0.5,  1,  0.0,   2,  1.5,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Antispin 3-Petal Down vs Inspin 1-Petal Up",         -2,  1.5,  1,  0.0,   2,  0.5,  1,  0),
    
    
    
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin 1-Petal Left vs Antispin 3-Petal Right",         2,  0.0,  1,  0.0,   2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin 1-Petal Right vs Antispin 3-Petal Left",         2,  1.0,  1,  0.0,   2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin 1-Petal Top vs Antispin 3-Petal Down",           2,  1.5,  1,  0.0,   2,  1.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin 1-Petal Bottom vs Antispin 3-Petal Up",          2,  0.5,  1,  0.0,   2,  0.5, -1,  1),
    
    PoiMove("Arms Tog/Opp Prop Tog/Same Antispin 3-Petal Left vs Inspin 1-Petal Right",        -2,  1.0,  1,  0.0,  -2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Antispin 3-Petal Right vs Inspin 1-Petal Left",        -2,  0.0,  1,  0.0,  -2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Antispin 3-Petal Up vs Inspin 1-Petal Bottom",         -2,  0.5,  1,  0.0,  -2,  0.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Tog/Same Antispin 3-Petal Down vs Inspin 1-Petal Top",          -2,  1.5,  1,  0.0,  -2,  1.5, -1,  1),

    PoiMove("Arms Tog/Opp Prop Split/Same Inspin 1-Petal Left vs Antispin 3-Petal Left",        2,  0.0,  1,  0.0,   2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Inspin 1-Petal Right vs Antispin 3-Petal Right",      2,  1.0,  1,  0.0,   2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Inspin 1-Petal Top vs Antispin 3-Petal Up",           2,  1.5,  1,  0.0,   2,  0.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Inspin 1-Petal Bottom vs Antispin 3-Petal Down",      2,  0.5,  1,  0.0,   2,  1.5, -1,  1),
    
    PoiMove("Arms Tog/Opp Prop Split/Same Antispin 3-Petal Left vs Inspin 1-Petal Left",       -2,  1.0,  1,  0.0,  -2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Antispin 3-Petal Right vs Inspin 1-Petal Right",     -2,  0.0,  1,  0.0,  -2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Antispin 3-Petal Up vs Inspin 1-Petal Top",          -2,  0.5,  1,  0.0,  -2,  1.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Same Antispin 3-Petal Down vs Inspin 1-Petal Bottom",     -2,  1.5,  1,  0.0,  -2,  0.5, -1,  1),

    PoiMove("Arms Tog/Opp Prop Split/Opp Inspin 1-Petal Left vs Inspin 1-Petal Left",          2,  0.0,  1,  0.0,  -2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Inspin 1-Petal Right vs Inspin 1-Petal Right",        2,  1.0,  1,  0.0,  -2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Inspin 1-Petal Top vs Inspin 1-Petal Bottom",         2,  1.5,  1,  0.0,  -2,  0.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Inspin 1-Petal Bottom vs Inspin 1-Petal Top",         2,  0.5,  1,  0.0,  -2,  1.5, -1,  1),
    
    PoiMove("Arms Tog/Opp Prop Split/Opp Antispin 3-Petal Left vs Antispin 3-Petal Left",     -2,  1.0,  1,  0.0,   2,  1.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Antispin 3-Petal Right vs Antispin 3-Petal Right",   -2,  0.0,  1,  0.0,   2,  0.0, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Antispin 3-Petal Up vs Antispin 3-Petal Down",       -2,  0.5,  1,  0.0,   2,  1.5, -1,  1),
    PoiMove("Arms Tog/Opp Prop Split/Opp Antispin 3-Petal Down vs Antispin 3-Petal Up",       -2,  1.5,  1,  0.0,   2,  0.5, -1,  1),

    PoiMove("Arms Split/Same Prop Tog/Same Inspin 1-Petal Left vs Inspin 1-Petal Left",        2,  0.0,  1,  0.0,   2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Inspin 1-Petal Right vs Inspin 1-Petal Right",      2,  1.0,  1,  0.0,   2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Inspin 1-Petal Up vs Inspin 1-Petal Down",          2,  1.5,  1,  0.0,   2,  1.5,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Inspin 1-Petal Down vs Inspin 1-Petal Up ",         2,  0.5,  1,  0.0,   2,  0.5,  1,  1),
    
    PoiMove("Arms Split/Same Prop Tog/Same Antispin 3-Petal Left vs Antispin 3-Petal Left",   -2,  0.0,  1,  0.0,  -2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Antispin 3-Petal Right vs Antispin 3-Petal Right", -2,  1.0,  1,  0.0,  -2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Antispin 3-Petal Up vs Antispin 3-Petal Up",       -2,  0.5,  1,  0.0,  -2,  0.5,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Same Antispin 3-Petal Down vs Antispin 3-Petal Down",   -2,  1.5,  1,  0.0,  -2,  1.5,  1,  1),
    
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin 1-Petal Left vs Antispin 3-Petal Left",       2,  0.0,  1,  0.0,  -2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin 1-Petal Right vs Antispin 3-Petal Right",     2,  1.0,  1,  0.0,  -2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin 1-Petal Top vs Antispin 3-Petal Down",        2,  1.5,  1,  0.0,  -2,  1.5,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin 1-Petal Bottom vs Antispin 3-Petal Up ",      2,  0.5,  1,  0.0,  -2,  0.5,  1,  1),
    
    PoiMove("Arms Split/Same Prop Tog/Opp Antispin 3-Petal Left vs Inspin 1-Petal Left",      -2,  0.0,  1,  0.0,   2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Antispin 3-Petal Right vs Inspin 1-Petal Right",    -2,  1.0,  1,  0.0,   2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Antispin 3-Petal Up vs Inspin 1-Petal Bottom",      -2,  0.5,  1,  0.0,   2,  0.5,  1,  1),
    PoiMove("Arms Split/Same Prop Tog/Opp Antispin 3-Petal Down vs Inspin 1-Petal Top",       -2,  1.5,  1,  0.0,   2,  1.5,  1,  1),
    
    PoiMove("Arms Split/Same Prop Split/Opp Inspin 1-Petal Left vs Antispin 3-Petal Right",     2,  0.0,  1,  0.0,  -2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Inspin 1-Petal Right vs Antispin 3-Petal Left",     2,  1.0,  1,  0.0,  -2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Inspin 1-Petal Top vs Antispin 3-Petal Up",         2,  1.5,  1,  0.0,  -2,  0.5,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Inspin 1-Petal Bottom vs Antispin 3-Petal Down ",   2,  0.5,  1,  0.0,  -2,  1.5,  1,  1),
    
    PoiMove("Arms Split/Same Prop Split/Opp Antispin 3-Petal Left vs Inspin 1-Petal Right",    -2,  0.0,  1,  0.0,   2,  0.0,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Antispin 3-Petal Right vs Inspin 1-Petal Left",    -2,  1.0,  1,  0.0,   2,  1.0,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Antispin 3-Petal Up vs Inspin 1-Petal Top",        -2,  0.5,  1,  0.0,   2,  1.5,  1,  1),
    PoiMove("Arms Split/Same Prop Split/Opp Antispin 3-Petal Down vs Inspin 1-Petal Bottom",   -2,  1.5,  1,  0.0,   2,  0.5,  1,  1),

    PoiMove("Arms Split/Opp Prop Tog/Same Inspin 1-Petal Left vs Antispin 3-Petal Right",       2,  0.0,  1,  0.0,   2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Inspin 1-Petal Right vs Antispin 3-Petal Left",       2,  1.0,  1,  0.0,   2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Inspin 1-Petal Top vs Antispin 3-Petal Down",         2,  1.5,  1,  0.0,   2,  1.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Inspin 1-Petal Bottom vs Antispin 3-Petal Up",        2,  0.5,  1,  0.0,   2,  0.5, -1,  0),
    
    PoiMove("Arms Split/Opp Prop Tog/Same Antispin 3-Petal Left vs Inspin 1-Petal Right",      -2,  1.0,  1,  0.0,  -2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Antispin 3-Petal Right vs Inspin 1-Petal Left",      -2,  0.0,  1,  0.0,  -2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Antispin 3-Petal Up vs Inspin 1-Petal Bottom",       -2,  0.5,  1,  0.0,  -2,  0.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Same Antispin 3-Petal Down vs Inspin 1-Petal Top",        -2,  1.5,  1,  0.0,  -2,  1.5, -1,  0),
    
    PoiMove("Arms Split/Opp Prop Tog/Opp Inspin 1-Petal Left vs Inspin 1-Petal Right",           2,  0.0,  1,  0.0,  -2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Inspin 1-Petal Right vs Inspin 1-Petal Left",           2,  1.0,  1,  0.0,  -2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Inspin 1-Petal Top vs Inspin 1-Petal Top",              2,  1.5,  1,  0.0,  -2,  1.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Inspin 1-Petal Bottom vs Inspin 1-Petal Bottom",        2,  0.5,  1,  0.0,  -2,  0.5, -1,  0),
    
    PoiMove("Arms Split/Opp Prop Tog/Opp Antispin 3-Petal Left vs Antispin 3-Petal Right",      -2,  1.0,  1,  0.0,   2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Antispin 3-Petal Right vs Antispin 3-Petal Left",      -2,  0.0,  1,  0.0,   2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Antispin 3-Petal Up vs Antispin 3-Petal Up",           -2,  0.5,  1,  0.0,   2,  0.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Tog/Opp Antispin 3-Petal Down vs Antispin 3-Petal Down",       -2,  1.5,  1,  0.0,   2,  1.5, -1,  0),
    
    PoiMove("Arms Split/Opp Prop Split/Same Inspin 1-Petal Left vs Antispin 3-Petal Left",        2,  0.0,  1,  0.0,   2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Inspin 1-Petal Right vs Antispin 3-Petal Left",       2,  1.0,  1,  0.0,   2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Inspin 1-Petal Top vs Antispin 3-Petal Up",           2,  1.5,  1,  0.0,   2,  0.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Inspin 1-Petal Bottom vs Antispin 3-Petal Down",      2,  0.5,  1,  0.0,   2,  1.5, -1,  0),
    
    PoiMove("Arms Split/Opp Prop Split/Same Antispin 3-Petal Left vs Inspin 1-Petal Right",      -2,  1.0,  1,  0.0,  -2,  0.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Antispin 3-Petal Right vs Inspin 1-Petal Left",      -2,  0.0,  1,  0.0,  -2,  1.0, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Antispin 3-Petal Up vs Inspin 1-Petal Top",          -2,  0.5,  1,  0.0,  -2,  1.5, -1,  0),
    PoiMove("Arms Split/Opp Prop Split/Same Antispin 3-Petal Down vs Inspin 1-Petal Bottom",     -2,  1.5,  1,  0.0,  -2,  0.5, -1,  0),
    
    # 3-Beat
    PoiMove("Tog/Opp Inspin Flower 2-Petal Top/Bottom",                              3,  0.0,  1,  0.0, -3,  1.0, -1,  1),
    PoiMove("Tog/Opp Inspin Flower 2-Petal Left/Right",                              3,  1.0,  1,  0.0, -3,  0.0, -1,  1),
    
    PoiMove("Split/Same Inspin Flower 2-Petal Top/Bottom",                           3,  1.0,  1,  1.0,  3,  0.0,  1,  0),
    PoiMove("Split/Same Inspin Flower 2-Petal Left/Right",                           3,  0.0,  1,  1.0,  3,  1.0,  1,  0),
    
    PoiMove("Split/Opp Inspin Flower 2-Petal Left/Right",                            3,  0.0,  1,  1.0, -3,  0.0, -1,  1),
    PoiMove("Split/Opp Inspin Flower 2-Petal Top/Bottom",                            3,  1.0,  1,  1.0, -3,  1.0, -1,  1),
    
    # Antispin Flowers
    PoiMove("Tog/Same Antispin Flower 4-Petal Diamond",                             -3,  0.0,  1,  0.0, -3,  0.0,  1,  0),
    PoiMove("Tog/Same Antispin Flower 4-Petal Box",                                 -3,  1.0,  1,  0.0, -3,  1.0,  1,  0),
    
    PoiMove("Tog/Opp Antispin Flower 4-Petal Diamond",                               3,  1.0, -1,  1.0, -3,  0.0,  1,  0),
    PoiMove("Tog/Opp Antispin Flower 4-Petal Box",                                   3,  0.0, -1,  1.0, -3,  1.0,  1,  0),
    
    PoiMove("Split/Same Antispin Flower 4-Petal Diamond",                           -3,  1.0,  1,  1.0, -3,  0.0,  1,  0),
    PoiMove("Split/Same Antispin Flower 4-Petal Box",                               -3,  0.0,  1,  1.0, -3,  1.0,  1,  0),
    
    PoiMove("Split/Opp Antispin Flower 4-Petal Diamond",                            -3,  0.0,  1,  0.0,  3,  0.0, -1,  0),    
    PoiMove("Split/Opp Antispin Flower 4-Petal Box",                                -3,  1.0,  1,  0.0,  3,  1.0, -1,  0),
    
    # # Hybrid Flowers
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin Top/Bottom vs Antispin Box",         -3,  0.0, -1,  0.0,  3,  1.0, -1,  0),    
    PoiMove("Arms Tog/Same Prop Tog/Opp Inspin Left/Right vs Antispin Diamond",     -3,  1.0, -1,  0.0,  3,  0.0, -1,  0),    
    PoiMove("Arms Tog/Same Prop Split/Same Inspin Left/Right vs Inspin Top/Bottom",  3,  1.0,  1,  0.0,  3,  0.0,  1,  0),    
    PoiMove("Arms Tog/Same Prop Split/Same Antispin Diamond vs Antispin Box",       -3,  0.0,  1,  0.0, -3,  1.0,  1,  0),
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin Top/Bottom vs Antispin Diamond",    3,  0.0,  1,  0.0, -3,  0.0,  1,  0), 
    PoiMove("Arms Tog/Same Prop Split/Opp Inspin Left/Right vs Antispin Box ",       3,  1.0,  1,  0.0, -3,  1.0,  1,  0), 
    
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin Top/Bottom vs Antispin Box",          3,  0.0,  1,  0.0,  3,  0.0, -1,  1),    
    PoiMove("Arms Tog/Opp Prop Tog/Same Inspin Left/Right vs Antispin Diamond",      3,  1.0,  1,  0.0,  3,  1.0, -1,  1),    
    PoiMove("Arms Tog/Opp Prop Split/Same Inspin Top/Bottom vs Antispin Diamond",    3,  0.0,  1,  0.0,  3,  1.0, -1,  1),    
    PoiMove("Arms Tog/Opp Prop Split/Same Inspin Left/Right vs Antispin Box",        3,  1.0,  1,  0.0,  3,  0.0, -1,  1),    
    PoiMove("Arms Tog/Opp Prop Split/Opp Inspin Top/Bottom vs Inspin Left/Right",    3,  0.0,  1,  0.0, -3,  0.0, -1,  1),    
    PoiMove("Arms Tog/Opp Prop Split/Opp Antispin Diamond vs Antispin Box",          3,  0.0, -1,  0.0, -3,  0.0,  1,  1),    
    
    PoiMove("Arms Split/Same Prop Tog/Same Inspin Top/Bottom vs Inspin Left/Right",  3,  0.0,  1,  0.0,  3,  0.0,  1,  1),    
    PoiMove("Arms Split/Same Prop Tog/Same Antispin Diamond vs Antispin Box",       -3,  0.0,  1,  0.0, -3,  0.0,  1,  1),    
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin Top/Bottom vs Antispin Diamond",    3,  0.0,  1,  0.0, -3,  1.0,  1,  1),    
    PoiMove("Arms Split/Same Prop Tog/Opp Inspin Left/Right vs Antispin Box ",       3,  1.0,  1,  0.0, -3,  0.0,  1,  1),    
    PoiMove("Arms Split/Same Prop Split/Opp Inspin Top/Bottom vs Antispin Box",      3,  0.0,  1,  0.0, -3,  0.0,  1,  1),    
    PoiMove("Arms Split/Same Prop Split/Opp Inspin Left/Right vs Antispin Diamond",  3,  1.0,  1,  0.0, -3,  1.0,  1,  1),    
    
    # Polyrithm Hybrids
    

]
