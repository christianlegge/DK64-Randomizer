// Donkey Kong 64 - Randomiser
// By theballaam96 & 2dos
// http://www.twitter.com/tjballaam
// http://www.twitter.com/2dos
// http://www.twitch.tv/iateyourpie/subscribe

// MIPS ASM
[ReturnAddress]: 0x807FFFE4
[ReturnAddress2]: 0x807FFFE8
[ReturnAddress3]: 0x807FFFEC

// Custom Variables
[BackupParentMap]: 0x807FFFDF // u8

// Normal Variables
[TransitionSpeed]: 0x807FD88C
[MovesBase]:  0x807FC950
[Gamemode]: 0x80755318
[StorySkip]: 0x8074452C
[TempFlagBlock]: 0x807FDD90
[CastleCannonPointer]: 0x807F5BE8
[ObjectTimer]: 0x8076A064
[CurrentMap]: 0x8076A0A8
[TroffNScoffReqArray]: 0x807446C0 // u16 item size
[BLockerDefaultArray]: 0x807446D0 // u16 item size
[BLockerCheatArray]: 0x807446E0 // u16 item size, [u8 - GB, u8 - Kong]
[ControllerInput]: 0x80014DC4
[NewlyPressedControllerInput]: 0x807ECD66
[CutsceneIndex]: 0x807476F4
[CutsceneActive]: 0x807444EC
[CutsceneTimer]: 0x807476F0
[ParentMap]: 0x8076A172
[ActorSpawnerArrayPointer]: 0x807FDC8C
[DestinationMap]: 0x807444E4
[DestinationExit]: 0x807444E8

// New Variables
[TestVariable]: 0x807FFFFC

// Functions
[SetFlag]: 0x8073129C
[DMAFileTransfer]: 0x80000450

// Loading Zones
[LZArray]: 0x807FDCB4 // u32
[LZSize]: 0x807FDCB0 // u16

// Pointers
[Player]: 0x807FBB4C
[SwapObject]: 0x807FC924
[Character]: 0x8074E77C

// Buttons
[L_Button]: 0x0020
[D_Up]: 0x0800
[D_Down]: 0x0400
[D_Left]: 0x0200
[D_Right]: 0x0100
[B_Button]: 0x4000
[A_Button]: 0x8000
[Z_Button]: 0x2000
[R_Button]: 0x0010
[Start_Button]: 0x1000

.org 0x805FC164 // retroben's hook but up a few functions
J Start

.org 0x8000072C // Boot
J   LoadInAdditionalFile
NOP

.org 0x8000DE88 // 0x00DE88 > 0x00EDDA. EDD1 seems the safe limit before overwriting data.

Start:
    // Run the code we replaced
    JAL     0x805FC2B0
    NOP
    JAL     RandoLevelOrder
    NOP
    JAL     UnlockKongs
    NOP
    JAL     GiveMoves
    NOP
    JAL     QOLChangesShorten
    NOP
    JAL     QOLChanges
    NOP
    JAL     SwapRequirements
    NOP
    JAL     SwapKeys
    NOP
    JAL     ChangeLZToHelm
    NOP
    JAL     OpenCoinDoor
    NOP
    JAL     OpenCrownDoor
    NOP
    JAL     TagAnywhere
    NOP

    Finish:
        J       0x805FC15C // retroben's hook but up a few functions
        NOP

.org 0x80000A30 // 0x000A30 > 0x0010BC

LoadInAdditionalFile:
    JAL     @DMAFileTransfer
    ADDIU   a0, a0, 0x13F0
    LI      a1, 0x20049A0
    LI      a2, 0x805DAE00
    JAL     @DMAFileTransfer       
    LUI     a0, 0x200 // 0x2000000
    J       0x80000734
    NOP

.org 0x805DAE00
// Randomize Level Progression
RandoLevelOrder:
    LA      a0, RandoOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, FinishSettingLZs
    NOP
    // Grab LZ Array (Size: 0x3A, Type: 0x10_u16, DMap: 0x12_u16, DExit: 0x14_dexit)
    LW      a0, @LZArray
    BEQZ    a0, FinishSettingLZs
    NOP
    LW      a1, @ObjectTimer
    LI      a2, 3
    BNE     a1, a2, FinishSettingLZs
    NOP
    LHU     a1, @LZSize
    LW      a2, @CurrentMap

    RandoLoop:
        // Lobby Entrances
        LA      t6, Lobbies
        LI      a3, 0x22 // Isles
        BNE     a2, a3, Exit
        LI      a3, 9 // Type
        LHU     t9, 0x10 (a0)
        BNE     t9, a3, LoopControl
        LI      t3, 0

        EntranceSearch:
            LA      t6, Lobbies
            ADD     t6, t6, t3
            LBU     t6, 0x0 (t6)
            LHU     t9, 0x12 (a0)
            BEQ     t6, t9, EntranceFound // t3 = lobby index
            NOP
            LI      t9, 7
            BEQ     t3, t9, LoopControl // Lobby index not found
            NOP
            B       EntranceSearch
            ADDIU   t3, t3, 1

        EntranceFound:
            LA      t6, LevelOrder
            ADD     t6, t6, t3
            LBU     t6, 0x0 (t6) // New Index
            LA      t3, Lobbies
            ADD     t3, t3, t6
            LBU     t3, 0x0 (t3) // New Lobby
            B       LoopControl
            SH      t3, 0x12 (a0)

        // Lobby Exits
        Exit:
            LHU     t9, 0x12 (a0)
            LI      a3, 0x22 // Isles
            BNE     t9, a3, LoopControl
            LI      a3, 9 // Type
            LHU     t9, 0x10 (a0)
            BNE     t9, a3, LoopControl
            LI      t3, 0

        ExitSearch:
            SW      t3, 0x807FFFF8
            LA      t6, Lobbies
            ADD     t6, t6, t3
            LBU     t6, 0x0 (t6)
            LW      t9, @CurrentMap
            BEQ     t6, t9, ExitFound // t3 = lobby index
            NOP
            LI      t9, 7
            BEQ     t3, t9, LoopControl // Lobby not found
            NOP
            ADDIU   t3, t3, 1
            B       ExitSearch
            NOP

        ExitFound:
            LI      t9, 0

        ExitFoundSearch:
            // t3 = Found Lobby
            // t9 = Index in Level Order
            SW      t9, @TestVariable
            LA      t6, LevelOrder
            ADD     t6, t6, t9
            LBU     t6, 0x0 (t6) // Source Index
            BEQ     t6, t3, ExitFoundIndexFound
            NOP
            LI      t6, 7
            BEQ     t9, t6, LoopControl // Index not found
            NOP
            ADDIU   t9, t9, 1
            B       ExitFoundSearch
            NOP

        ExitFoundIndexFound:
            LA      t3, LobbyExits
            ADD     t3, t3, t9
            LBU     t3, 0x0 (t3) // Found Exit Value
            SH      t3, 0x14 (a0)

        // Loop Control
        LoopControl:
            ADDI    a1, a1, -1
            BEQZ    a1, CastleCannon
            ADDIU   a0, a0, 0x3A
            B       RandoLoop
            NOP

    CastleCannon:
        LW      a0, @CurrentMap
        LI      a1, 0x22
        BNE     a0, a1, FinishSettingLZs
        NOP
        LW      a0, @CastleCannonPointer
        BEQZ    a0, FinishSettingLZs
        SRA     a1, a0, 16
        SLTIU   a2, a1, 0x8000
        BNEZ    a2, FinishSettingLZs
        SLTIU   a2, a1, 0x8080
        BEQZ    a2, FinishSettingLZs
        NOP
        LHU     a1, 0x376 (a0)
        LI      a2, 0x22
        BNE     a1, a2, FinishSettingLZs
        NOP
        LA      a1, LevelOrder
        LBU     a1, 0x6 (a1) // Castle Cannon Lobby Index
        LA      a2, Lobbies
        ADD     a2, a2, a1
        LBU     a2, 0x0 (a2) // Cannon Map
        SH      a2, 0x378 (a0)

    // We are going with randomized level lobby entrances
        // Values of lobby entrances
        // Values of lobby exits
        // Determine level order from randomized array in python script
            // Each level would need its B Locker value, T&S value and Key value adjusted to
            // what level number it is

    FinishSettingLZs:
        JR      ra
        NOP

// Swap B. Locker/Cheat Code/T&S counts
SwapRequirements:
    LA      a0, RandoOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, SwapRequirements_Finish
    NOP
    LBU     a0, @TransitionSpeed
    ANDI    a0, a0, 0x80
    BEQZ    a0, SwapRequirements_Finish
    NOP
    LA      a0, TroffNScoffAmounts
    LA      a1, BLockerDefaultAmounts
    LA      a2, BLockerCheatAmounts
    LI      t3, 0
    LI      t7, 8

    SwapRequirements_Loop:
        // T&S
        LI      t9, @TroffNScoffReqArray
        SLL     t6, t3, 1
        ADD     t9, t9, t6
        LHU     t6, 0x0 (a0)
        SH      t6, 0x0 (t9)
        // B. Locker Default
        LI      t9, @BLockerDefaultArray
        SLL     t6, t3, 1
        ADD     t9, t9, t6
        LHU     t6, 0x0 (a1)
        SH      t6, 0x0 (t9)
        // B. Locker Cheat
        LI      t9, @BLockerCheatArray
        SLL     t6, t3, 1
        ADD     t9, t9, t6
        LHU     t6, 0x0 (a2)
        SB      t6, 0x0 (t9)
        // Loop
        ADDI    t7, t7 -1
        BEQZ    t7, SwapRequirements_Finish
        ADDIU   a0, a0, 2
        ADDIU   a1, a1, 2
        ADDIU   a2, a2, 2
        B       SwapRequirements_Loop
        ADDIU   t3, t3, 1

    SwapRequirements_Finish:
        JR      ra
        NOP

// Swap Keys around
SwapKeys:
    LA      a0, RandoOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, SwapKeys_Finish
    NOP
    LBU     a0, @TransitionSpeed
    ANDI    a0, a0, 0x80
    BEQZ    a0, SwapKeys_Finish
    NOP
    LA      a0, KeyMaps
    LW      a1, @CurrentMap
    LI      a2, 7

    SwapKeys_MapLoop:
        LBU     t0, 0x0 (a0)
        BEQ     t0, a1, SwapKeys_SetKeys
        ADDI    a2, a2, -1
        BEQZ    a2, SwapKeys_Finish
        ADDIU   a0, a0, 1
        B       SwapKeys_MapLoop
        NOP

    SwapKeys_SetKeys:
        LA      a0, KeyAddress
        LA      a1, KeyFlags
        LI      a2, 7

    SwapKeys_SetKeysLoop:
        LW      t0, 0x0 (a0)
        LHU     t3, 0x0 (a1)
        SH      t3, 0x0 (t0)
        ADDI    a2, a2, -1
        BEQZ    a2, SwapKeys_Finish
        ADDIU   a0, a0, 4
        B       SwapKeys_SetKeysLoop
        ADDIU   a1, a1, 2        

    SwapKeys_Finish:
        JR      ra
        NOP
    

// Unlock All Kongs - OPTIONAL
UnlockKongs:
    SW      ra, @ReturnAddress
    LA      a0, KongFlags
    JAL     SetAllFlags
    NOP
    LW      ra, @ReturnAddress
    JR      ra
    NOP

// Unlock All Moves - OPTIONAL
GiveMoves:
    SW      ra, @ReturnAddress
    LA      a0, UnlockAllMoves
    LBU     a0, 0x0 (a0)
    BEQZ    a0, GiveMoves_Finish
    NOP
    LI      a0, 4
    LI      a1, @MovesBase
    WriteMoves:
        LI      t3, 0x0303
        SH      t3, 0x0 (a1) // Special | Slam Level | Guns | Ammo Belt
        LA      t3, SniperValue
        LBU     t3, 0x0 (t3)
        SB      t3, 0x2 (a1) // Gun Bitfield
        LI      t3, 0x2
        SB      t3, 0x3 (a1) // Ammo belt
        LI      t3, 15
        SB      t3, 0x4 (a1) // Instrument
        BEQZ    a0, WriteMoveFlags
        ADDI    a0, a0, -1 // Decrement Value for next kong
        B       WriteMoves
        ADDIU   a1, a1, 0x5E // Next kong base
    
    WriteMoveFlags:
        JAL     CodedSetPermFlag
        LI      a0, 0x179 // BFI Camera

    GiveMoves_Finish:
        LW      ra, @ReturnAddress
        JR      ra
        NOP

// Enable Tag Anywhere - OPTIONAL
TagAnywhere:
    LA      a0, TagAnywhereOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, TagAnywhere_Finish
    NOP
    LH      a1, @NewlyPressedControllerInput
    ANDI    a2, a1, @D_Left
    BNEZ    a2, TagAnywhere_ChangeCharacter
    LI      t0, -1
    ANDI    a2, a1, @D_Right
    BNEZ    a2, TagAnywhere_ChangeCharacter
    LI      t0, 1
    B       TagAnywhere_Finish
    NOP

    TagAnywhere_ChangeCharacter:
        LBU     a2, @Character
        LI      t3, 1
        BEQ     t0, t3, TagAnywhere_Add // Inc Kong
        NOP
        BEQZ    a2, WrapAround_Neg
        NOP
        B       GunCheck
        ADDI    a2, a2, -1

    TagAnywhere_Add:
        SLTIU   t8, a2, 4
        BEQZ    t8, WrapAround_Pos
        NOP
        B       GunCheck
        ADDIU   a2, a2, 1 // New Character Value

    WrapAround_Neg:
        B       GunCheck
        LI      a2, 4

    WrapAround_Pos:
        LI      a2, 0

    GunCheck:
        LW      a1, @Player
        BEQZ    a1, TagAnywhere_Finish // If player isn't in RDRAM, cancel
        NOP
        LA      a3, GunBitfields
        SLL     t3, a2, 2 // new_kong x 4
        ADD     a3, t3, a3
        LW      a3, 0x0 (a3)
        LBU     t9, 0x0 (a3) // Get gun bitfield for kong
        ANDI    t9, t9, 1 // Has gun
        BEQZ    t9, RetractGun
        NOP
        LBU     t9, 0x20C(a1) // Was gun out
        BEQZ    t9, RetractGun
        NOP

    PullOutGun:
        LA      t9, HandStatesGun
        ADD     t9, t9, a2
        LBU     t9, 0x0 (t9)
        SB      t9, 0x147 (a1) // Set Hand State
        LI      t9, 1
        B       ChangeCharacter
        SB      t9, 0x20C (a1) // Set Gun State

    RetractGun:
        LA      t9, HandStatesNoGun
        ADD     t9, t9, a2
        LBU     t9, 0x0 (t9)
        SB      t9, 0x147 (a1) // Set Hand State
        SB      r0, 0x20C (a1) // Set Gun State

    ChangeCharacter:
        LW      a1, @Player
        BEQZ    a1, TagAnywhere_Finish // If player isn't in RDRAM, cancel
        ADDIU   a2, a2, 2
        SB      a2, 0x36F (a1)
        LW      a1, @SwapObject
        BEQZ    a1, TagAnywhere_Finish // If swap object isn't in RDRAM, cancel
        LI      a2, 0x3B
        SH      a2, 0x29C (a1) // Initiate Swap

    TagAnywhere_Finish:
        JR      ra
        NOP

// Shorter Helm
// Spawn in Blast-o-Matic Area
ChangeLZToHelm:
    SW      ra, @ReturnAddress
    LA      a0, ShorterHelmOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, ChangeLZToHelm_Finish
    NOP
    LW      a0, @CurrentMap
    LI      a1, 0xAA
    BNE     a0, a1, ChangeLZToHelm_Finish
    NOP
    LW      a0, @ObjectTimer
    LI      a1, 3
    BNE     a0, a1, ChangeLZToHelm_Finish
    NOP
    LW      a0, @LZArray
    LHU     a1, @LZSize

    ChangeLZToHelm_CheckLZ:
        LHU     a2, 0x10 (a0)
        LI      a3, 9
        BNE     a2, a3, ChangeLZToHelm_Enumerate
        NOP
        LHU     a2, 0x12 (a0)
        LI      a3, 0x11
        BNE     a2, a3, ChangeLZToHelm_Enumerate
        NOP
        LHU     a2, 0x14 (a0)
        BNEZ    a2, ChangeLZToHelm_Enumerate
        NOP
        LI      a3, 3
        SH      a3, 0x14 (a0)
        // Story: Helm
        JAL     CodedSetPermFlag
        LI      a0, 0x1CC
        // Open I-II-III-IV-V doors
        LI      a0, 0x3B
        LI      a1, 1
        JAL     @SetFlag
        LI      a2, 2
        // Gates knocked down
        LI      a0, 0x46
        LI      a1, 1
        JAL     @SetFlag
        LI      a2, 2
        LI      a0, 0x47
        LI      a1, 1
        JAL     @SetFlag
        LI      a2, 2
        LI      a0, 0x48
        LI      a1, 1
        JAL     @SetFlag
        LI      a2, 2
        LI      a0, 0x49
        LI      a1, 1
        JAL     @SetFlag
        LI      a2, 2
        B       ChangeLZToHelm_Finish
        NOP

    ChangeLZToHelm_Enumerate:
        ADDIU   a0, a0, 0x3A
        ADDI    a1, a1, -1
        BEQZ    a1, ChangeLZToHelm_Finish
        NOP
        B       ChangeLZToHelm_CheckLZ
        NOP

    ChangeLZToHelm_Finish:
        LW      ra, @ReturnAddress
        JR      ra
        NOP


// Open Crown door
OpenCrownDoor:
    SW      ra, @ReturnAddress
    LA      a0, ShorterHelmOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, OpenCrownDoor_Finish
    NOP
    JAL     CodedSetPermFlag
    LI      a0, 0x304
    
    OpenCrownDoor_Finish:
        LW      ra, @ReturnAddress
        JR      ra
        NOP
    
// Open Rareware + Nintendo Coin door (Give both coins)
OpenCoinDoor:
    SW      ra, @ReturnAddress
    LA      a0, ShorterHelmOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, OpenCoinDoor_Finish
    NOP
    JAL     CodedSetPermFlag
    LI      a0, 0x84
    JAL     CodedSetPermFlag
    LI      a0, 0x17B
    JAL     CodedSetPermFlag
    LI      a0, 0x303

    OpenCoinDoor_Finish:
        LW      ra, @ReturnAddress
        JR      ra
        NOP

// QoL Changes that require the "Shorten Cutscenes" option to be on
QOLChangesShorten:
    SW          ra, @ReturnAddress
    LA          a0, QualityChangesOn
    LBU         a0, 0x0 (a0)
    BEQZ        a0, FinishQOLShorten
    NOP

    // Remove First Time Text
    NoFTT:
        LA      a0, FTTFlags
        JAL     SetAllFlags
        NOP

    NoDance:
        SW      r0, 0x806EFB9C // Movement Write
        SW      r0, 0x806EFC1C // CS Play
        SW      r0, 0x806EFB88 // Animation Write
        SW      r0, 0x806EFC0C // Change Rotation
        SW      r0, 0x806EFBA8 // Control State Progress

    // Remove First Time Boss Cutscenes
    ShortenBossCutscenes:
        LI      a1, @TempFlagBlock
        LI      a2, 0x803F // All Boss Cutscenes
        SH      a2, 0xC (a1)

    // Shorter Snides Cutscenes
    SnidesCutsceneCompression:
        // The cutscene the game chooses is based on the parent map (the method used to detect which Snide's H.Q. you're in)
        // The shortest contraption cutscene is chosen with parent map 0
        // So we swap out the original parent map with 0 at the right moment to get short cutscenes
        // Then swap the original value back in at the right moment so that the player isn't taken back to test map when exiting Snide's H.Q.
        LW      t0, @CurrentMap
        LI      t1, 0xF
        BNE     t0, t1, FinishQOLShorten
        NOP
        LHU     t0, @CutsceneIndex
        LI      t1, 5
        BEQ     t0, t1, SnidesCutsceneCompression_CS5
        NOP
        LI      t1, 2
        BEQ     t0, t1, SnidesCutsceneCompression_CS2
        NOP
        B       SnidesCutsceneCompression_TurnIn
        NOP

        SnidesCutsceneCompression_CS5:
            LHU     t0, @CutsceneTimer
            LI      t1, 199
            BEQ     t0, t1, SnidesCutsceneCompression_Time199
            NOP
            LI      t1, 200
            BEQ     t0, t1, SnidesCutsceneCompression_Time200
            NOP
            B       SnidesCutsceneCompression_TurnIn
            NOP

            SnidesCutsceneCompression_Time199:
                // Make a backup copy of the current parent map to restore later
                LHU     t2, @ParentMap
                SB      t2, @BackupParentMap
                B       SnidesCutsceneCompression_TurnIn
                NOP

            SnidesCutsceneCompression_Time200:
                // Set parent map to 0
                SH      r0, @ParentMap
                B       SnidesCutsceneCompression_TurnIn
                NOP

        SnidesCutsceneCompression_CS2:
            // Restore the backup copy of the parent map
            LBU     t2, @BackupParentMap
            SH      t2, @ParentMap

        SnidesCutsceneCompression_TurnIn:
            // Dereference the spawner array
            LW      t0, @ActorSpawnerArrayPointer
            BEQZ    t0, FinishQOLShorten // If there's no array loaded, don't bother
            NOP

            SnidesCutsceneCompression_TurnIn_Loop:
                // Find a snide entry (enemy type 7)
                LBU     t1, 0x0 (t0) // Get enemy type at slot 0
                LI      t2, 7 // Snide Enemy Type
                BNE     t1, t2, FinishQOLShorten
                NOP

                // Dereference the Snide Actor pointer from it
                LW      t0, 0x18 (t0)
                BEQZ    t0, FinishQOLShorten
                NOP

                // Read the turn count (Snide + 0x232)
                LBU     t1, 0x232 (t0)
                BEQZ    t1, FinishQOLShorten
                NOP
                LI      t2, 1
                SB      t2, 0x232 (t0)

    FinishQOLShorten:
        LW      ra, @ReturnAddress
        JR      ra
        NOP

// Loops through a flag array and sets all of them
// Credit: Isotarge (Tag Anywhere V5)
SetAllFlags:
    // Params:
    // a0 = Array
    ADDIU   sp, sp, -0x18 // Push S0
    SW      s0, 0x10(sp)
    SW      ra, 0x14(sp)
    NOP

    // Load flag array base into register to loop with
    ADDIU   s0, a0, 0

    SetAllFlagsLoop:
        LHU     a0, 0(s0) // Load the flag index from the array
        BEQZ    a0, FinishSettingAllFlags // If the flag index is 0, exit the loop
        NOP
        JAL     CodedSetPermFlag
        NOP
        B       SetAllFlagsLoop
        ADDIU   s0, s0, 2 // Move on to the next flag in the array

    FinishSettingAllFlags:
        LW      s0, 0x10(sp)  // Pop S0
        LW      ra, 0x14(sp)
        JR
        ADDIU   sp, sp, 0x18

QOLChanges:
    SW      ra, @ReturnAddress
    LA      a0, QualityChangesOn
    LBU     a0, 0x0 (a0)
    BEQZ    a0, FinishQOL
    NOP
    // Remove DK Rap from startup
    FridgeHasBeenTaken:
        LI       a1, 0x50
        SB       a1, 0x807132BF // Set Destination Map after N/R Logos to Main Menu
        LI       a1, 5
        SB       a1, 0x807132CB // Set Gamemode after N/R Logos to Main Menu Mode

    // Story Skip set to "On" by default (not locked to On)
    StorySkip:
        LBU     a1, @Gamemode
        BNEZ    a1, FastStart
        NOP
        LI      a1, 1
        SB      a1, @StorySkip

    // Start with training barrels complete + simian slam (start in DK Isles spawn)
    FastStart:
        LA      a0, FastStartFlags
        JAL     SetAllFlags
        NOP
        // Slam
        LI      a0, 4
        LI      a1, @MovesBase
        LBU     a2, 0x1(a1)
        BNEZ    a2, IslesSpawn
        NOP
        
        WriteSlam:
            LI      t3, 0x1
            SB      t3, 0x1 (a1) // Slam Level 1
            BEQZ    a0, IslesSpawn
            ADDI    a0, a0, -1 // Decrement Value for next kong
            B       WriteSlam
            ADDIU   a1, a1, 0x5E // Next kong base

        // Isles Spawn
        IslesSpawn:
        SW      r0, 0x80714540 // Cancels check

    FinishQOL:
        LW      ra, @ReturnAddress
        JR      ra
        NOP

// Bulk of set flag code
CodedSetPermFlag:
    // a0 is parameter for encoded flag
    SW      ra, @ReturnAddress3
    LI      a1, 1
    JAL     @SetFlag
    LI      a2, 0
    LW      ra, @ReturnAddress3
    JR      ra
    NOP

.align
GunBitfields:
    .word 0x807FC952 // DK
    .word 0x807FC9B0 // Diddy
    .word 0x807FCA0E // Lanky
    .word 0x807FCA6C // Tiny
    .word 0x807FCACA // Chunky

.align
HandStatesNoGun:
    .byte 1 // DK
    .byte 0 // Diddy
    .byte 1 // Lanky
    .byte 1 // Tiny
    .byte 1 // Chunky

.align
HandStatesGun:
    .byte 2 // DK
    .byte 3 // Diddy
    .byte 2 // Lanky
    .byte 2 // Tiny
    .byte 2 // Chunky

.align
KeyAddress:
    .word 0x800258FA
    .word 0x8002C136
    .word 0x80035676
    .word 0x8002A0C2
    .word 0x8002B3F6
    .word 0x80025C4E
    .word 0x800327EE

.align
KeyMaps:
    .byte 0x08
    .byte 0xC5
    .byte 0x9A
    .byte 0x6F
    .byte 0x53
    .byte 0xC4
    .byte 0xC7

.align
FTTFlags:
    .half 355 // Bananaporter
    .half 358 // Crown Pad
    .half 359 // T&S (1)
    .half 360 // Mini Monkey
    .half 361 // Hunky Chunky
    .half 362 // Orangstand Sprint
    .half 363 // Strong Kong
    .half 364 // Rainbow Coin
    .half 365 // Rambi
    .half 366 // Enguarde
    .half 367 // Diddy
    .half 368 // Lanky
    .half 369 // Tiny
    .half 370 // Chunky
    .half 372 // Snide's
    .half 373 // Buy Instruments
    .half 374 // Buy Guns
    .half 376 // Wrinkly
    .half 382 // B Locker
    .half 392 // T&S (2)
    .half 775 // Funky
    .half 776 // Snide's
    .half 777 // Cranky
    .half 778 // Candy
    .half 779 // Japes
    .half 780 // Factory
    .half 781 // Galleon
    .half 782 // Fungi
    .half 783 // Caves
    .half 784 // Castle
    .half 785 // T&S (3)
    .half 786 // Helm
    .half 787 // Aztec
    .half 282 // Caves CS
    .half 194 // Galleon CS
    .half 256 // Daytime
    .half 257 // Fungi CS
    .half 303 // DK 5DI
    .half 349 // Castle CS
    .half 27 // Japes CS
    .half 95 // Aztec CS
    .half 93 // Lanky Help Me
    .half 94 // Tiny Help Me
    .half 140 // Chunky Help Me / Factory CS
    .half 195 // Water Raised
    .half 196 // Water Lowered
    .half 255 // Clock CS
    .half 277 // Rotating Room
    .half 299 // Giant Kosha
    .half 378 // Training Grounds Intro
    .half 0 // Null Terminator

.align
Lobbies:
    .byte 0xA9 // Japes
    .byte 0xAD // Aztec
    .byte 0xAF // Factory
    .byte 0xAE // Galleon
    .byte 0xB2 // Fungi
    .byte 0xC2 // Caves
    .byte 0xC1 // Castle
    .byte 0xAA // Helm
    .byte 0x00 // Terminator

.align
LobbyExits:
    .byte 0x2 // Japes
    .byte 0x3 // Aztec
    .byte 0x4 // Factory
    .byte 0x5 // Galleon
    .byte 0x6 // Fungi
    .byte 0xA // Caves
    .byte 0xB // Castle
    .byte 0x7 // Helm
    .byte 0x0 // Terminator

.align
LevelOrder:
    .byte 0
    .byte 2
    .byte 5
    .byte 3
    .byte 1
    .byte 6
    .byte 4
    .byte 7

.align
FastStartFlags:
    .half 386
    .half 387
    .half 388
    .half 389
    .half 377
    .half 0