/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/*!
 * \file codegen_nnp_intrisic_info_inc.h
 * \brief NNP400 nu instruction desciption.
 */

#ifndef TVM_TARGET_EDGEX_CODEGEN_NNP_INTRINSIC_INFO_INC_H_
#define TVM_TARGET_EDGEX_CODEGEN_NNP_INTRINSIC_INFO_INC_H_

{llvm::Intrinsic::nnp_cube_loop_times,
 {"zeta_times_cube", "dense_times_cube", "delta_times_cube", "num_group_cube"}},
    {llvm::Intrinsic::nnp_cube_loop0,
     {"delta_cube", "zeta_cube", "dense_cube", "epsilon_times_cube"}},
    {llvm::Intrinsic::nnp_cube_loop1, {"last_beta_remind_cube", "epsilon_cube"}},
    {llvm::Intrinsic::nnp_cube_last_loop,
     {"last_dense_cube", "last_zeta_cube", "last_delta_cube", "last_epsilon_cube"}},
    {llvm::Intrinsic::nnp_cube_k_size, {"k_size_cube"}},
    {llvm::Intrinsic::nnp_cube_burst_size, {"burst_size_pipe_num_cube"}},
    {llvm::Intrinsic::nnp_cube_bias_value, {"bias_value_cube"}},
    {llvm::Intrinsic::nnp_cube_layer_burst,
     {"obuf_wait_cyc_num_clr_cube",
      "sbuf_wait_cyc_num_clr_cube",
      "wbuf_wait_cyc_num_clr_cube",
      "ibuf_wait_cyc_num_clr_cube",
      "bbuf_wait_cyc_num_clr_cube",
      "warm_up_times_clr_cube",
      "nan_warning_clr_cube",
      "inf_warning_clr_cube",
      "overflow_warning_clr_cube",
      "result_mode_cube",
      "psum_mode_cube",
      "float_mode_cube",
      "round_mode_cube",
      "bias_mode_cube",
      "delta_rewrite_nbbuf_cube",
      "dense_times_rewrite_ibuf_cube",
      "epsilon_rewrite_ibuf_cube",
      "epsilon_times_rewrite_wbuf_cube",
      "delta_rewrite_wbuf_cube",
      "weight_type_cube",
      "data_type_cube",
      "bias_en_cube",
      "sparsity_en_cube",
      "winograd_cube",
      "cube_work_num_cube"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg0,
     {"op_idma", "dense_idma", "zeta_idma", "delta_idma", "epsilon_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg1,
     {"para_mode_idma", "delta_times_idma", "dense_times_idma", "zeta_times_idma",
      "epsilon_times_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg2,
     {"wino_en_idma", "last_dense_idma", "last_zeta_idma", "last_delta_idma", "last_epsilon_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg3,
     {"kernel1_speedup_flag_idma", "sparsity_en_idma", "d_d_idma", "d_h_idma", "d_w_idma",
      "s_d_idma", "s_h_idma", "s_w_idma", "k_d_idma", "k_h_idma", "k_w_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg4,
     {"epsilon_rewrite_ibuf_idma", "dense_times_rewrite_ibuf_idma", "last_zeta_width_idma",
      "ci_d_idma", "ci_h_idma", "ci_w_idma", "cube_enable_idma", "data_type_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg5,
     {"eps_ci_times_idma", "co_d_idma", "co_h_idma", "co_w_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg6, {"pad_v_idma", "num_group_idma", "num_ci_group_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg7,
     {"pad_mode_idma", "pad_bh_idma", "pad_f_idma", "pad_r_idma", "pad_l_idma", "pad_b_idma",
      "pad_t_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_cfg8,
     {"last_eps_ci_times_idma", "insert_d0_idma", "insert_h0_idma", "insert_w0_idma", "B_T_idma",
      "B_dim2_idma", "B_dim1_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_addr0,
     {"addr_wrap_sel2_idma", "addr_wrap_sel1_idma", "start_addr_sel_idma", "feat_end_addr1_idma",
      "feat_st_addr1_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_addr1, {"ci_row_offset_idma", "ci_ch_offset_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_addr2, {"ci_dense_offset_idma", "group_offset_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_addr3, {"feat_end_addr2_idma", "feat_st_addr2_idma"}},
    {llvm::Intrinsic::nnp_idma_warmup_cfg, {"deconv_insert_value_idma", "xbar_urr_weight_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_ub,
     {"ub_eidma_idma",
      "ub_odma_idma",
      "state0_ub_vcu0_vodma0_idma",
      "state0_ub_vcu1_vodma1_idma",
      "state0_ub_vcu2_vodma2_idma",
      "state0_ub_vcu3_vodma3_idma",
      "state1_ub_vcu0_vodma0_idma",
      "state1_ub_vcu1_vodma1_idma",
      "state1_ub_vcu2_vodma2_idma",
      "state1_ub_vcu3_vodma3_idma",
      "state2_ub_vcu0_vodma0_idma",
      "state2_ub_vcu1_vodma1_idma",
      "state2_ub_vcu2_vodma2_idma",
      "state2_ub_vcu3_vodma3_idma",
      "state3_ub_vcu0_vodma0_idma",
      "state3_ub_vcu1_vodma1_idma",
      "state3_ub_vcu2_vodma2_idma",
      "state3_ub_vcu3_vodma3_idma",
      "vcu_vodma_ub_sel_idma",
      "ub_ewdma_idma",
      "ub_tdma_idma",
      "start_state_mode_idma",
      "ub_ci_num_idma"}},
    {llvm::Intrinsic::nnp_idma_layer_burst,
     {"wo_eidma_idma",
      "wo_odma_idma",
      "state0_wo_vcu0_vodma0_idma",
      "state0_wo_vcu1_vodma1_idma",
      "state0_wo_vcu2_vodma2_idma",
      "state0_wo_vcu3_vodma3_idma",
      "state1_wo_vcu0_vodma0_idma",
      "state1_wo_vcu1_vodma1_idma",
      "state1_wo_vcu2_vodma2_idma",
      "state1_wo_vcu3_vodma3_idma",
      "state2_wo_vcu0_vodma0_idma",
      "state2_wo_vcu1_vodma1_idma",
      "state2_wo_vcu2_vodma2_idma",
      "state2_wo_vcu3_vodma3_idma",
      "state3_wo_vcu0_vodma0_idma",
      "state3_wo_vcu1_vodma1_idma",
      "state3_wo_vcu2_vodma2_idma",
      "state3_wo_vcu3_vodma3_idma",
      "vcu_vodma_wo_sel_idma",
      "wo_ewdma_idma",
      "wo_tdma_idma",
      "end_state_idma",
      "wo_h_num_idma",
      "wo_d_num_idma",
      "wo_ci_num_idma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg0,
     {"dense_times_odma", "zeta_times_odma", "dense_odma", "zeta_odma", "delta_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg1,
     {"last_delta_co_odma", "last_zeta_width_odma", "last_dense_odma", "last_zeta_odma",
      "last_delta_odma", "delta_times_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg2,
     {"num_group_odma", "co_d_odma", "co_h_odma", "co_w_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg3,
     {"addr_wrap_sel2_odma", "addr_wrap_sel1_odma", "start_addr_sel_odma", "rslt_end_addr1_odma",
      "rslt_st_addr1_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg4,
     {"extract_2to1_odma", "int_type_odma", "para_mode_odma", "delta_mode_odma", "psum_out_en_odma",
      "norm_coeff_mode_odma", "xbar_urr_weight_odma", "relu_en_odma", "round_mode_odma",
      "delta_rewrite_nbuf_odma", "op_odma", "wino_en_odma", "cube_enable_odma", "bias_en_odma",
      "data_type_odma", "relu_mode_odma", "leaky_relu_mode_odma", "bias_mode_odma",
      "relu_round_mode_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg5,
     {"relu_sftcoeff_odma", "relu_mulcoeff_odma", "bias_value_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg6,
     {"zeta_offset_odma", "wino_zeta_add_en_odma", "init_xbar_wr_byte_odma",
      "last_xbar_co_times_odma", "last_xbar_pixel_times_odma", "last_xbar_wr_byte_odma",
      "last_xbar_cube_times_odma", "delta_times_transfer_co_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_addr0, {"rslt_end_addr2_odma", "rslt_st_addr2_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_addr1, {"co_ch_offset_odma", "co_dense_offset_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_addr2, {"delta_ch_offset_odma", "co_group_offset_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_ub,
     {"ub_eodma_odma",
      "ub_idma_odma",
      "state0_ub_vcu0_vidma0_odma",
      "state0_ub_vcu1_vidma1_odma",
      "state0_ub_vcu2_vidma2_odma",
      "state0_ub_vcu3_vidma3_odma",
      "state1_ub_vcu0_vidma0_odma",
      "state1_ub_vcu1_vidma1_odma",
      "state1_ub_vcu2_vidma2_odma",
      "state1_ub_vcu3_vidma3_odma",
      "state2_ub_vcu0_vidma0_odma",
      "state2_ub_vcu1_vidma1_odma",
      "state2_ub_vcu2_vidma2_odma",
      "state2_ub_vcu3_vidma3_odma",
      "state3_ub_vcu0_vidma0_odma",
      "state3_ub_vcu1_vidma1_odma",
      "state3_ub_vcu2_vidma2_odma",
      "state3_ub_vcu3_vidma3_odma",
      "vcu_vidma_ub_sel_odma",
      "ub_tdma_odma",
      "start_state_mode_odma",
      "ub_channel_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_burst,
     {"wo_eodma_odma",
      "wo_idma_odma",
      "state0_wo_vcu0_vidma0_odma",
      "state0_wo_vcu1_vidma1_odma",
      "state0_wo_vcu2_vidma2_odma",
      "state0_wo_vcu3_vidma3_odma",
      "state1_wo_vcu0_vidma0_odma",
      "state1_wo_vcu1_vidma1_odma",
      "state1_wo_vcu2_vidma2_odma",
      "state1_wo_vcu3_vidma3_odma",
      "state2_wo_vcu0_vidma0_odma",
      "state2_wo_vcu1_vidma1_odma",
      "state2_wo_vcu2_vidma2_odma",
      "state2_wo_vcu3_vidma3_odma",
      "state3_wo_vcu0_vidma0_odma",
      "state3_wo_vcu1_vidma1_odma",
      "state3_wo_vcu2_vidma2_odma",
      "state3_wo_vcu3_vidma3_odma",
      "vcu_vidma_wo_sel_odma",
      "wo_tdma_odma",
      "end_state_odma",
      "wo_channel_odma"}},
    {llvm::Intrinsic::nnp_odma_layer_cfg7, {"shiftnorm_odma", "mulnorm_odma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg0,
     {"sparsity_en_wdma", "dense_wdma", "zeta_wdma", "delta_wdma", "epsilon_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg1,
     {"bubble_insert_en_wdma", "delta_times_wdma", "dense_times_wdma", "zeta_times_wdma",
      "epsilon_times_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg2,
     {"operation_wdma", "last_dense_wdma", "last_zeta_wdma", "last_delta_wdma",
      "last_epsilon_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg3,
     {"data_type_wdma", "para_mode_wdma", "cube_enable_wdma", "rotate_en_wdma", "num_group_wdma",
      "A_transpose_wdma", "A_dim2_wdma", "A_dim1_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_addr0,
     {"wt_addr_wrap_sel2_wdma", "wt_addr_wrap_sel1_wdma", "wt_st_addr_sel_wdma", "st_addr_en_wdma",
      "wt_end_addr1_wdma", "wt_st_addr1_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_addr1,
     {"cb_mode_en_wdma", "wt_end_addr2_wdma", "wt_st_addr2_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_addr2,
     {"delta_bubble_inc_addr_wdma", "epsilon_bubble_inc_addr_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_addr3,
     {"spar_addr_wrap_sel2_wdma", "spar_addr_wrap_sel1_wdma", "spar_st_addr_sel_wdma",
      "spar_ind_end_addr1_wdma", "spar_ind_st_addr1_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_addr4, {"spar_ind_end_addr2_wdma", "spar_ind_st_addr2_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg4,
     {"epsilon_times_rewrite_dm_wdma", "epsilon_times_rewrite_wbuf_wdma", "delta_rewrite_wbuf_wdma",
      "k_size_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg5, {"ksize_inc_addr_wdma", "delta_inc_addr_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_cfg6, {"delta_times_inc_addr_wdma", "epstimes_inc_addr_wdma"}},
    {llvm::Intrinsic::nnp_wdma_warmup_cfg,
     {"warm_up_en_wdma", "xbar_urr_weight_wdma", "mat_row_offset_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_ub,
     {"ub_ewdma_wdma",
      "ub_eidma_wdma",
      "state0_ub_vcu0_vodma0_wdma",
      "state0_ub_vcu1_vodma1_wdma",
      "state0_ub_vcu2_vodma2_wdma",
      "state0_ub_vcu3_vodma3_wdma",
      "state1_ub_vcu0_vodma0_wdma",
      "state1_ub_vcu1_vodma1_wdma",
      "state1_ub_vcu2_vodma2_wdma",
      "state1_ub_vcu3_vodma3_wdma",
      "state2_ub_vcu0_vodma0_wdma",
      "state2_ub_vcu1_vodma1_wdma",
      "state2_ub_vcu2_vodma2_wdma",
      "state2_ub_vcu3_vodma3_wdma",
      "state3_ub_vcu0_vodma0_wdma",
      "state3_ub_vcu1_vodma1_wdma",
      "state3_ub_vcu2_vodma2_wdma",
      "state3_ub_vcu3_vodma3_wdma",
      "vcu_vodma_ub_sel_wdma",
      "ub_tdma_wdma",
      "start_state_mode_wdma",
      "ub_data_len_wdma"}},
    {llvm::Intrinsic::nnp_wdma_layer_burst,
     {"wo_ewdma_wdma",
      "wo_eidma_wdma",
      "state0_wo_vcu0_vodma0_wdma",
      "state0_wo_vcu1_vodma1_wdma",
      "state0_wo_vcu2_vodma2_wdma",
      "state0_wo_vcu3_vodma3_wdma",
      "state1_wo_vcu0_vodma0_wdma",
      "state1_wo_vcu1_vodma1_wdma",
      "state1_wo_vcu2_vodma2_wdma",
      "state1_wo_vcu3_vodma3_wdma",
      "state2_wo_vcu0_vodma0_wdma",
      "state2_wo_vcu1_vodma1_wdma",
      "state2_wo_vcu2_vodma2_wdma",
      "state2_wo_vcu3_vodma3_wdma",
      "state3_wo_vcu0_vodma0_wdma",
      "state3_wo_vcu1_vodma1_wdma",
      "state3_wo_vcu2_vodma2_wdma",
      "state3_wo_vcu3_vodma3_wdma",
      "vcu_vodma_wo_sel_wdma",
      "wo_tdma_wdma",
      "end_state_wdma",
      "wo_data_len_wdma"}},
    {llvm::Intrinsic::nnp_bdma_addr1, {"end_addr1_bdma", "st_addr1_bdma"}},
    {llvm::Intrinsic::nnp_bdma_addr2,
     {"addr_wrap_sel2", "addr_wrap_sel1", "st_addr_sel", "end_addr2_bdma", "st_addr2_bdma"}},
    {llvm::Intrinsic::nnp_bdma_loop0,
     {"zeta_times_bdma", "dense_times_bdma", "delta_times_bdma", "num_group_bdma"}},
    {llvm::Intrinsic::nnp_bdma_loop1,
     {"delta_bdma", "zeta_bdma", "dense_bdma", "epsilon_times_bdma"}},
    {llvm::Intrinsic::nnp_bdma_last_loop, {"last_dense_bdma", "last_zeta_bdma", "last_delta_bdma"}},
    {llvm::Intrinsic::nnp_bdma_layer_burst,
     {"leaky_relu_mode_bdma",
      "leaky_relu_en_bdma",
      "norm_coeff_mode_bdma",
      "bias_mode_bdma",
      "port_urgent_bdma",
      "ub_vodma3_bdma",
      "ub_vodma2_bdma",
      "ub_vodma1_bdma",
      "ub_vodma0_bdma",
      "ub_vcu3_bdma",
      "ub_vcu2_bdma",
      "ub_vcu1_bdma",
      "ub_vcu0_bdma",
      "ub_cu_bdma",
      "ub_ewdma_bdma",
      "ub_eidma_bdma",
      "wo_vodma3_bdma",
      "wo_vodma2_bdma",
      "wo_vodma1_bdma",
      "wo_vodma0_bdma",
      "wo_vcu3_bdma",
      "wo_vcu2_bdma",
      "wo_vcu1_bdma",
      "wo_vcu0_bdma",
      "wo_cu_bdma",
      "wo_ewdma_bdma",
      "wo_eidma_bdma",
      "winograd_bdma",
      "delta_rewrite_nbbuf_bdma",
      "norm_en_bdma",
      "bias_en_bdma",
      "parallel_mode_bdma",
      "cube_work_num_bdma"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg0,
     {"ei_axi_prio", "ei_crop", "ei_cb_buf", "ei_sub_offset", "ei_mode", "ei_state_num",
      "ei_first_state_en", "ei_start_addr_out_en", "ei_start_addr_in_en", "ei_dtype"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg1, {"ei_src_index_addr", "ei_src_index_addr_high"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg2, {"ei_src_addr", "ei_src_addr_high"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg3,
     {"ei_addr_wrap_sel2", "ei_addr_wrap_sel1", "ei_start_addr2", "ei_st_addr_sel",
      "ei_end_addr2"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg4,
     {"ei_axi_arcache", "ei_read_size", "ei_j0_loop_sel", "ei_j1_loop_sel", "ei_j2_loop_sel",
      "ei_j3_loop_sel"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg5, {"ei_j2_loop_num", "ei_j3_loop_num"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg6, {"ei_j0_loop_num", "ei_j1_loop_num"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg7, {"ei_j2_stridein", "ei_ub_dense"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg8, {"ei_j1_stridein", "ei_ub_ci"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg9, {"ei_j0_stridein", "ei_ub_line"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg10, {"ei_end_addr1", "ei_start_addr1"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg11, {"ei_j2_strideout", "ei_j0_strideout"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg12,
     {"ei_outstanding_num", "ei_qos_num", "ei_qos_en", "ei_j1_strideout"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg13, {"ei_wo_data_size", "ei_ub_data_size"}},
    {llvm::Intrinsic::nnp_eidma_layer_cfg14, {"ei_const_pad_data", "ei_urgency"}},
    {llvm::Intrinsic::nnp_eidma_layer_burst,
     {"ei_ub_tdma", "ei_wo_tdma", "ei_ub_wdma", "ei_ub_bdma", "ei_ub_idma", "ei_ub_vidma",
      "ei_ub_vcu", "ei_ub_cu", "ei_wo_vidma", "ei_state3", "ei_state2", "ei_state1", "ei_state0",
      "ei_wo_vcu", "ei_wo_wdma", "ei_wo_bdma", "ei_wo_eodma", "ei_wo_idma", "ei_wo_cu"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg0,
     {"eo_first_state_en", "eo_state_num", "eo_dtype", "eo_j0_loop_sel", "eo_j1_loop_sel",
      "eo_j2_loop_sel", "eo_j3_loop_sel", "eo_start_addr_out_en", "eo_cb_buf", "eo_crop"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg1, {"eo_dst_index_addr", "eo_dst_index_addr_high"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg2, {"eo_dst_addr", "eo_dst_addr_high"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg3,
     {"eo_j3_loop_num", "eo_axi_awcache", "eo_mode", "eo_start_addr_in_en", "eo_outstanding_num",
      "eo_qos_num", "eo_qos_en"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg4,
     {"eo_st_addr_sel", "eo_start_addr1", "eo_addr_wrap_sel1", "eo_addr_wrap_sel2",
      "eo_end_addr1"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg5, {"eo_start_addr2", "eo_end_addr2"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg6, {"eo_j1_loop_num", "eo_j2_loop_num"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg7, {"eo_stride_in_j2", "eo_j0_loop_num"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg8, {"eo_stride_in_j0", "eo_stride_in_j1"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg9, {"eo_j0_strideout", "eo_aw_sideband"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg10, {"eo_j1_strideout"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg11, {"eo_j2_strideout", "eo_urgency"}},
    {llvm::Intrinsic::nnp_eodma_layer_cfg12, {"eo_wo_data_size", "eo_ub_data_size"}},
    {llvm::Intrinsic::nnp_eodma_layer_burst,
     {"eo_state3", "eo_state2", "eo_state1", "eo_state0", "eo_wo_tdma", "eo_ub_tdma", "eo_ub_vodma",
      "eo_ub_vcu", "eo_wo_vodma", "eo_wo_vcu", "eo_ub_ewdma", "eo_ub_eidma", "eo_ub_odma",
      "eo_ub_cu", "eo_wo_odma", "eo_wo_cu", "eo_axi_prio"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg0,
     {"ew_axi_arcache", "ew_urgency", "ew_axi_prio", "ew_cb_buf", "ew_mode", "ew_state_num",
      "ew_first_state_en", "ew_dtype", "ew_start_addr_out_en", "ew_start_addr_in_en"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg1, {"ew_sps_start_addr2", "ew_sps_end_addr2"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg2, {"ew_src_addr", "ew_src_addr_high"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg3, {"ew_src_index_addr", "ew_src_index_addr_high"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg4,
     {"ew_addr_wrap_sel1", "ew_addr_wrap_sel2", "ew_start_addr1", "ew_sps_addr_wrap_sel1",
      "ew_sps_addr_wrap_sel2", "ew_end_addr1", "ew_st_addr_sel"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg5, {"ew_start_addr2", "ew_end_addr2"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg6, {"ew_sps_start_addr1", "ew_sps_end_addr1"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg7, {"ew_j3_loop_num"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg8, {"ew_wo_data_size", "ew_ub_data_size"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg9, {"ew_j1_stridein", "ew_j2_stridein"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg10, {"ew_j2_strideout", "ew_j1_strideout"}},
    {llvm::Intrinsic::nnp_ewdma_layer_cfg11, {"ew_j1_loop_num", "ew_j2_loop_num"}},
    {llvm::Intrinsic::nnp_ewdma_layer_burst,
     {"ew_wo_tdma", "ew_ub_tdma", "ew_outstanding_num", "ew_qos_num",  "ew_qos_en",  "ew_ub_bdma",
      "ew_ub_wdma", "ew_ub_idma", "ew_ub_vidma",        "ew_ub_vcu",   "ew_ub_cu",   "ew_state3",
      "ew_state2",  "ew_state1",  "ew_state0",          "ew_wo_eodma", "ew_wo_idma", "ew_wo_vidma",
      "ew_wo_vcu",  "ew_wo_bdma", "ew_wo_wdma",         "ew_wo_cu"}},
    {llvm::Intrinsic::nnp_xbar_layer_burst,
     {"cool_down_cyc", "bg_warmup_cyc_xbar", "inner_warmup_cyc_xbar"}},
    {llvm::Intrinsic::nnp_sync, {"bb", "wo", "bb1"}},
    {llvm::Intrinsic::nnp_checkpoint, {"bb", "ckp_id"}},
    {llvm::Intrinsic::nnp_urgent, {"bb", "arb_urgent"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg0,
     {"nlfc_mem_en_vidma", "const_wr_en_vidma", "j3_loop_sel_vidma", "j2_loop_sel_vidma",
      "j1_loop_sel_vidma", "j0_loop_sel_vidma", "crop_en_vidma", "cb_buf_dm_vidma",
      "cb_buf_vm_vidma", "start_addr_out_en_vidma", "start_addr_in_en_vidma", "dtype_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg1, {"const_wdata_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg2, {"j2_loop_num_vidma", "j3_loop_num_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg3, {"j0_loop_num_vidma", "j1_loop_num_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg4,
     {"j2_stridein_vidma", "dm_addr_wrap_sel2_vidma", "dm_addr_wrap_sel1_vidma",
      "dm_st_addr_sel_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg5, {"j1_stridein_vidma", "wrap_start_addr_vm_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg6, {"j0_stridein_vidma", "port_urgent_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg7, {"end_addr1_dm_vidma", "start_addr1_dm_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg8,
     {"cb_buf_end_addr_vm_vidma", "cb_buf_start_addr_vm_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg9, {"j1_strideout_vidma", "j2_strideout_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg10, {"ub_data_size_dm_vidma", "j0_strideout_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg11, {"ub_data_size_vm_vidma", "wo_data_size_dm_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_cfg12, {"end_addr2_dm_vidma", "start_addr2_dm_vidma"}},
    {llvm::Intrinsic::nnp_vidma_layer_burst,
     {"wo_data_size_vm_vidma", "ub_tdma_vidma", "wo_tdma_vidma", "ub_vodma_vidma", "ub_odma_vidma",
      "ub_ewdma_vidma", "ub_eidma_vidma", "ub_vcu_vidma", "wo_vodma_vidma", "wo_odma_vidma",
      "wo_ewdma_vidma", "wo_eidma_vidma", "wo_vcu_vidma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg0,
     {"const_wr_en_vodma", "j3_loop_sel_vodma", "j2_loop_sel_vodma", "j1_loop_sel_vodma",
      "j0_loop_sel_vodma", "crop_en_vodma", "cb_buf_dm_vodma", "cb_buf_vm_vodma",
      "start_addr_out_en_vodma", "start_addr_in_en_vodma", "dtype_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg1, {"const_wdata_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg2, {"j2_loop_num_vodma", "j3_loop_num_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg3, {"j0_loop_num_vodma", "j1_loop_num_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg4,
     {"j2_stridein_vodma", "dm_addr_wrap_sel2_vodma", "dm_addr_wrap_sel1_vodma",
      "dm_st_addr_sel_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg5, {"j1_stridein_vodma", "wrap_start_addr_vm_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg6, {"j0_stridein_vodma", "port_urgent_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg7, {"end_addr1_dm_vodma", "start_addr1_dm_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg8,
     {"cb_buf_end_addr_vm_vodma", "cb_buf_start_addr_vm_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg9, {"j1_strideout_vodma", "j2_strideout_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg10, {"ub_data_size_dm_vodma", "j0_strideout_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg11, {"ub_data_size_vm_vodma", "wo_data_size_dm_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_cfg12, {"end_addr2_dm_vodma", "start_addr2_dm_vodma"}},
    {llvm::Intrinsic::nnp_vodma_layer_burst,
     {"wo_data_size_vm_vodma", "ub_tdma_vodma", "wo_tdma_vodma", "ub_bdma_vodma", "ub_vidma_vodma",
      "ub_wdma_vodma", "ub_idma_vodma", "ub_eodma_vodma", "ub_vcu_vodma", "wo_bdma_vodma",
      "wo_vidma_vodma", "wo_wdma_vodma", "wo_idma_vodma", "wo_eodma_vodma", "wo_vcu_vodma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg0,
     {"const_wr_en_tdma", "j3_loop_sel_tdma", "j2_loop_sel_tdma", "j1_loop_sel_tdma",
      "j0_loop_sel_tdma", "crop_en_tdma", "start_addr_out_en_tdma", "start_addr_in_en_tdma",
      "dtype_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg1, {"const_wdata_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg2, {"j2_loop_num_tdma", "j3_loop_num_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg3, {"j0_loop_num_tdma", "j1_loop_num_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg4,
     {"j2_stridein_tdma", "rd_dm_addr_wrap_sel2_tdma", "rd_dm_addr_wrap_sel1_tdma",
      "rd_dm_st_addr_sel_tdma", "wr_dm_addr_wrap_sel2_tdma", "wr_dm_addr_wrap_sel1_tdma",
      "wr_dm_st_addr_sel_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg5, {"j1_stridein_tdma", "j0_strideout_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg6,
     {"j0_stridein_tdma", "wr_port_urgent_tdma", "rd_port_urgent_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg7, {"rd_end_addr1_dm_tdma", "rd_start_addr1_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg8, {"wr_end_addr1_dm_tdma", "wr_start_addr1_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg9, {"j1_strideout_tdma", "j2_strideout_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg10, {"rd_ub_data_size_dm_tdma", "rd_wo_data_size_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg11, {"wr_ub_data_size_dm_tdma", "wr_wo_data_size_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg12, {"rd_end_addr2_dm_tdma", "rd_start_addr2_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg13, {"wr_end_addr2_dm_tdma", "wr_start_addr2_dm_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_cfg14,
     {"wr_start_state_mode_tdma",
      "rd_start_state_mode_tdma",
      "ub_wdma_tdma",
      "ub_idma_tdma",
      "ub_odma_tdma",
      "ub_eodma_tdma",
      "ub_ewdma_tdma",
      "ub_eidma_tdma",
      "ub_state3_vcu3_vidma3_tdma",
      "ub_state3_vcu2_vidma2_tdma",
      "ub_state3_vcu1_vidma1_tdma",
      "ub_state3_vcu0_vidma0_tdma",
      "ub_state2_vcu3_vidma3_tdma",
      "ub_state2_vcu2_vidma2_tdma",
      "ub_state2_vcu1_vidma1_tdma",
      "ub_state2_vcu0_vidma0_tdma",
      "ub_state1_vcu3_vidma3_tdma",
      "ub_state1_vcu2_vidma2_tdma",
      "ub_state1_vcu1_vidma1_tdma",
      "ub_state1_vcu0_vidma0_tdma",
      "ub_state0_vcu3_vidma3_tdma",
      "ub_state0_vcu2_vidma2_tdma",
      "ub_state0_vcu1_vidma1_tdma",
      "ub_state0_vcu0_vidma0_tdma",
      "ub_vcu_vidma_sel_tdma",
      "ub_state3_vcu3_vodma3_tdma",
      "ub_state3_vcu2_vodma2_tdma",
      "ub_state3_vcu1_vodma1_tdma",
      "ub_state3_vcu0_vodma0_tdma",
      "ub_state2_vcu3_vodma3_tdma",
      "ub_state2_vcu2_vodma2_tdma",
      "ub_state2_vcu1_vodma1_tdma",
      "ub_state2_vcu0_vodma0_tdma",
      "ub_state1_vcu3_vodma3_tdma",
      "ub_state1_vcu2_vodma2_tdma",
      "ub_state1_vcu1_vodma1_tdma",
      "ub_state1_vcu0_vodma0_tdma",
      "ub_state0_vcu3_vodma3_tdma",
      "ub_state0_vcu2_vodma2_tdma",
      "ub_state0_vcu1_vodma1_tdma",
      "ub_state0_vcu0_vodma0_tdma",
      "ub_vcu_vodma_sel_tdma"}},
    {llvm::Intrinsic::nnp_tdma_layer_burst,
     {"wr_end_state_tdma",
      "rd_end_state_tdma",
      "wo_wdma_tdma",
      "wo_idma_tdma",
      "wo_odma_tdma",
      "wo_eodma_tdma",
      "wo_ewdma_tdma",
      "wo_eidma_tdma",
      "wo_state3_vcu3_vidma3_tdma",
      "wo_state3_vcu2_vidma2_tdma",
      "wo_state3_vcu1_vidma1_tdma",
      "wo_state3_vcu0_vidma0_tdma",
      "wo_state2_vcu3_vidma3_tdma",
      "wo_state2_vcu2_vidma2_tdma",
      "wo_state2_vcu1_vidma1_tdma",
      "wo_state2_vcu0_vidma0_tdma",
      "wo_state1_vcu3_vidma3_tdma",
      "wo_state1_vcu2_vidma2_tdma",
      "wo_state1_vcu1_vidma1_tdma",
      "wo_state1_vcu0_vidma0_tdma",
      "wo_state0_vcu3_vidma3_tdma",
      "wo_state0_vcu2_vidma2_tdma",
      "wo_state0_vcu1_vidma1_tdma",
      "wo_state0_vcu0_vidma0_tdma",
      "wo_vcu_vidma_sel_tdma",
      "wo_state3_vcu3_vodma3_tdma",
      "wo_state3_vcu2_vodma2_tdma",
      "wo_state3_vcu1_vodma1_tdma",
      "wo_state3_vcu0_vodma0_tdma",
      "wo_state2_vcu3_vodma3_tdma",
      "wo_state2_vcu2_vodma2_tdma",
      "wo_state2_vcu1_vodma1_tdma",
      "wo_state2_vcu0_vodma0_tdma",
      "wo_state1_vcu3_vodma3_tdma",
      "wo_state1_vcu2_vodma2_tdma",
      "wo_state1_vcu1_vodma1_tdma",
      "wo_state1_vcu0_vodma0_tdma",
      "wo_state0_vcu3_vodma3_tdma",
      "wo_state0_vcu2_vodma2_tdma",
      "wo_state0_vcu1_vodma1_tdma",
      "wo_state0_vcu0_vodma0_tdma",
      "wo_vcu_vodma_sel_tdma"}},

#endif  // TVM_TARGET_EDGEX_CODEGEN_NNP_INTRINSIC_INFO_INC_H_
